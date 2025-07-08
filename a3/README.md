In config.txt
  Change the first line to your port id
  Change the second line to the port id of the next device in the ring

Make sure all users are on the same wifi
Run myleprocess.py in the correct ring order.

Log1
Sent: uuid=462eb82a-13c0-4335-b54f-3a23b0690776, flag=0
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0, greater, 0
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1, greater, 0
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1
Leader is decided to be2ba45c-3715-44fe-a152-aa369e01a8bc
Leader is be2ba45c-3715-44fe-a152-aa369e01a8bc

Log2
Received: uuid=462eb82a-13c0-4335-b54f-3a23b0690776, flag=0, less, 0
Ignored smaller UUID
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0, greater, 0
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1, greater, 0
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1
Leader is decided to be2ba45c-3715-44fe-a152-aa369e01a8bc
Sent: uuid=97b91968-6ded-43cf-8901-ce1cc94509e2, flag=0
Leader is be2ba45c-3715-44fe-a152-aa369e01a8bc

Log3
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=0, same, 0
Leader is decided to be2ba45c-3715-44fe-a152-aa369e01a8bc
Sent: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1
Received: uuid=be2ba45c-3715-44fe-a152-aa369e01a8bc, flag=1, same, 1, leader_id=be2ba45c-3715-44fe-a152-aa369e01a8bc
Leader is decided to be2ba45c-3715-44fe-a152-aa369e01a8bc
Received: uuid=97b91968-6ded-43cf-8901-ce1cc94509e2, flag=0, less, 1, leader_id=be2ba45c-3715-44fe-a152-aa369e01a8bc
Ignored smaller UUID
Leader is be2ba45c-3715-44fe-a152-aa369e01a8bc
