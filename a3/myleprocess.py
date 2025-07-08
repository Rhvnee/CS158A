import time
from node import Node

if __name__ == "__main__":
    node = Node("config.txt")
    node.start()

    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down.")
