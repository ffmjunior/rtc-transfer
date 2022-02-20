# RTC-transfer

File transfer based on WebRTC based on [aiortc datachannel-filexfer](https://github.com/aiortc/aiortc/tree/main/examples/datachannel-filexfer) and the signaling server from [libdatachannel](https://github.com/paullouisageneau/libdatachannel/tree/master/examples/signaling-server-python)

## Requirements

Up to Python 3.8 (depends on netifaces)

`pip3 install aiortc websockets pystray tk `

# Usage

Start the server on a endpoint accessible from both endpoints. Ideally, the server has public IP/address

`python3 ./signaling-server.py 0.0.0.0:9000`

Start the receiver. Arguments are server-addres, server-port, a 'receive' statement and the file name to save (it may or may not be equal to the original file).

It will generate a 4-digit code. After that, press enter do skip the input for peer code.

`python3 rtc-transfer.py --host [server-address] --port [server-port] receive [filename]`

Finally, start the sender. Arguments are server-addres, server-port, a 'send' statement and the file name to send.

When it starts, type the 4-digit code generated on the receiver. 

`python3 rtc-transfer.py --host [server-address] --port [server-port] send [filename]`

# Backlog
- Manage memory utilization on signaling server
- Automatic definition of sender and receiver
- UI
- Progress bar for the download
