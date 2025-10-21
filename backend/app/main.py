from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from .ws import websocket_endpoint

app = FastAPI(title="AI Multiplayer Game")

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "AI Multiplayer Game API is running"}

@app.websocket("/ws/{player_id}")
async def ws_player(websocket: WebSocket, player_id: str):
    await websocket_endpoint(websocket, player_id)
