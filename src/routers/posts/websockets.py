from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import WebSocket

websocket_connections: set[WebSocket] = set()


async def broadcast_list(session: AsyncSession):
    for connection in websocket_connections:

        pass
