from fastapi import WebSocket
from .game_logic import GameManager

game_manager = GameManager()

async def websocket_endpoint(websocket: WebSocket, player_id: str):
    await game_manager.connect(websocket, player_id)
    try:
        while True:
            data = await websocket.receive_text()
            await game_manager.receive(player_id, data)
    except:
        game_manager.disconnect(player_id)
