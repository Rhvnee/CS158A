import socket
import threading
import time
import uuid
import os
from message import Message

class Node:

    def __init__(self, config_path="config.txt"):

        self.uuid = uuid.uuid4()
        self.leader_id = None
        self.state = 0
        self.conn = None
        self.last_message_time = None  #set after first message
        self.timeout_seconds = 10 #seconds of no messages being sent until termination
        self.log_file = open("log.txt", "w") #send logs
        self.load_config(config_path)

    def load_config(self, path):

        with open(path) as f:

            lines = f.read().strip().splitlines()

        self.my_ip, my_port = lines[0].split(",")
        neighbor_ip, neighbor_port = lines[1].split(",")

        self.my_port = int(my_port)
        self.neighbor = (neighbor_ip.strip(), int(neighbor_port.strip()))

    def log(self, text):

        print(text)
        self.log_file.write(text + "\n")
        self.log_file.flush()

    def message_handler(self, msg):

        self.last_message_time = time.time()

        cmp = "same" if msg.uuid == str(self.uuid) else "greater" if msg.uuid > str(self.uuid) else "less"

        self.log(f"Received: uuid={msg.uuid}, flag={msg.flag}, {cmp}, {self.state}" +
                 (f", leader_id={self.leader_id}" if self.state == 1 else ""))

        if msg.flag == 1:

            self.leader_id = msg.uuid

            if self.state == 0:

                self.state = 1
                self.send_message(msg)

            self.log(f"Leader is decided to {self.leader_id}")

        elif msg.uuid == str(self.uuid):

            self.state = 1
            self.leader_id = str(self.uuid)

            self.log(f"Leader is decided to {self.leader_id}")
            msg.flag = 1
            self.send_message(msg)

        elif msg.uuid > str(self.uuid):

            self.send_message(msg)

        else:

            self.log("Ignored smaller UUID")

    def send_message(self, msg):
        if self.conn:

            try:

                self.conn.sendall(msg.to_json().encode())
                self.log(f"Sent: uuid={msg.uuid}, flag={msg.flag}")

            except Exception as e:

                self.log(f"Failed to send message: {e}")

    def start_server_thread(self):

        def handle_client(conn):

            buffer = ""

            while True:

                try:

                    data = conn.recv(1024).decode()

                    if not data:

                        break

                    buffer += data

                    while "\n" in buffer:

                        line, buffer = buffer.split("\n", 1)
                        msg = Message.from_json(line)
                        self.message_handler(msg)

                except:

                    break

            conn.close()

        def server():

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind((self.my_ip, self.my_port))
            s.listen(1)

            conn, _ = s.accept()
            threading.Thread(target=handle_client, args=(conn,)).start()

        threading.Thread(target=server, daemon=True).start()

    def connect_to_neighbor(self):

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        while True:

            try:

                s.connect(self.neighbor)
                break

            except:

                time.sleep(1)

        self.conn = s

    def monitor_timeout(self):

        while True:

            if self.last_message_time is None:

                continue  #wait until first message sent

            if time.time() - self.last_message_time > self.timeout_seconds:

                if self.leader_id:

                    self.log(f"Leader is {self.leader_id}")


                else:

                    self.log("Leader not determined before timeout.")


                self.log_file.close()

                if self.conn:

                    self.conn.close()

                os._exit(0)  #force exit from any
            time.sleep(1)

    def start(self):

        self.start_server_thread()
        self.connect_to_neighbor()

        time.sleep(2)
        initial_message = Message(self.uuid, 0)

        self.send_message(initial_message)
        self.last_message_time = time.time()  #start timer after send
        threading.Thread(target=self.monitor_timeout, daemon=True).start()
