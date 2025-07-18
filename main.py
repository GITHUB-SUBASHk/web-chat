import os
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware 
from dotnev import load_dotnev

#load from .env
load_dotenv()

PORT= int(os.getenv("PORT",10000))
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS","*").split(",")

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all for now
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get():
    with open("static/index.html") as f:
        return HTMLResponse(f.read())


# Chat server part
clients = []

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_text("NICKNAME")
    nickname = await websocket.receive_text()
    clients.append((websocket, nickname))
    await broadcast(f"{nickname} joined the chat.")

    try:
        while True:
            data = await websocket.receive_text()
            await broadcast(data, sender=websocket)
    except WebSocketDisconnect:
        clients.remove((websocket, nickname))
        await broadcast(f"{nickname} left the chat.")

async def broadcast(message: str, sender=None):
    for conn, _ in clients:
        if conn != sender:
            await conn.send_text(message)
