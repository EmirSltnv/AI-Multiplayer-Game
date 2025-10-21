import asyncio
import random
from .models import Player, GameState

class GameManager:
    def __init__(self):
        self.players = {}
        self.state = GameState()
    
    async def connect(self, websocket, player_id):
        player = Player(id=player_id, name=player_id)
        self.players[player_id] = {"websocket": websocket, "player": player}
        self.state.players[player_id] = player
        await websocket.send_text(f"Welcome {player_id}!")

    async def receive(self, player_id, message):
        # Update player position (demo: simple numeric move)
        player = self.players[player_id]["player"]
        if message == "move_forward":
            player.position += 1
        elif message == "move_backward":
            player.position -= 1
        player.position = max(0, min(player.position, self.state.max_position))

        # Broadcast updated state to all players
        await self.broadcast_state()

        # AI bot move
        ai_action = random.choice(["move_forward", "move_backward"])
        await self.ai_move("AI_Bot", ai_action)

    async def ai_move(self, bot_id, action):
        if bot_id not in self.state.players:
            self.state.players[bot_id] = Player(id=bot_id, name=bot_id)
        bot = self.state.players[bot_id]
        if action == "move_forward":
            bot.position += 1
        else:
            bot.position -= 1
        bot.position = max(0, min(bot.position, self.state.max_position))
        await self.broadcast_state()

    async def broadcast_state(self):
        state_summary = {pid: {"position": p.position, "score": p.score} for pid, p in self.state.players.items()}
        for ws_data in self.players.values():
            try:
                await ws_data["websocket"].send_text(str(state_summary))
            except:
                pass

    def disconnect(self, player_id):
        if player_id in self.players:
            del self.players[player_id]
        if player_id in self.state.players:
            del self.state.players[player_id]
