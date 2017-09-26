import asyncio
import websockets
import json
async def status():
    async with websockets.connect('ws://127.0.0.1:4040/_ws') as websocket:

        resp = await websocket.recv()
        json_obj = json.loads(resp)
        payload = (json_obj["Payload"])
        tunnel = (json_obj["Payload"]["Tunnels"]["command_line"]["URL"])
        print(tunnel)
asyncio.get_event_loop().run_until_complete(status())