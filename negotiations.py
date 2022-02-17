import asyncio
import json
import uuid

from aiortc import RTCIceCandidate, RTCPeerConnection, RTCSessionDescription, sdp
from aiortc.contrib.signaling import BYE

try:
    import websockets
except ImportError:  # pragma: no cover
    aiohttp = None
    websockets = None

def remove_peer_id(message_str):
    message = json.loads(message_str)
    peer = message["peer_id"]
    del message["peer_id"]    
    return peer, json.dumps(message)

def add_peer_id(message_str, peer_id):
    message = json.loads(message_str)
    message["peer_id"] = peer_id    
    return json.dumps(message)

def object_from_string(message_str):
    message = json.loads(message_str)
    if message["type"] in ["answer", "offer"]:
        return RTCSessionDescription(**message)
    elif message["type"] == "candidate" and message["candidate"]:
        candidate = sdp.candidate_from_sdp(message["candidate"].split(":", 1)[1])
        candidate.sdpMid = message["id"]
        candidate.sdpMLineIndex = message["label"]
        return candidate
    elif message["type"] == "bye":
        return BYE


def object_to_string(obj, peer_id = ""):
    if isinstance(obj, RTCSessionDescription):
        message = {"sdp": obj.sdp, "type": obj.type, "peer_id":peer_id}
    elif isinstance(obj, RTCIceCandidate):
        message = {
            "candidate": "candidate:" + sdp.candidate_to_sdp(obj),
            "id": obj.sdpMid,
            "label": obj.sdpMLineIndex,
            "type": "candidate",
            "peer_id":peer_id,
        }
    else:
        assert obj is BYE
        message = {"type": "bye"}
    return json.dumps(message, sort_keys=True)


class WebSocketSignaling:
    def __init__(self, host, port, client_id, peer_id):               
        self._server = f"ws://{host}:{port}/{client_id}" # "https://appr.tc"        
        self._websocket = None
        self._peer = peer_id

    async def connect(self):
        # connect to websocket
        self._websocket = await websockets.connect( self._server)        

    async def close(self):
        pass 
        # if self._websocket:
        #     await self.send(BYE)
        #     await self._websocket.close()

    async def receive(self):        
        message = await self._websocket.recv()        
        #logger.info("< " + message)
        print("\n\n< " + message)
        self._peer, message = remove_peer_id(message)        
        return object_from_string(message)

    async def send(self, obj):
        message = object_to_string(obj, self._peer)
        message = add_peer_id(message, self._peer)
        #logger.info("> " + message)
        print("\n\n> " + message)
        await self._websocket.send(message)
