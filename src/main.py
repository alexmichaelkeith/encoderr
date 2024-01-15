import asyncio
import os
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from src.tasks import periodic, scan
from pathlib import Path
from src.api.utils import get_root_folder
from fastapi.middleware.cors import CORSMiddleware
from src.utils.logger import setup_logger
from src.api.routes import (
    codec_routes,
    profile_routes,
    scan_routes,
    series_routes,
    settings_routes,
    season_routes,
    system_routes,
    websocket_routes
)

# Create app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Add Routes
routers = [
    season_routes.router,
    scan_routes.router,
    settings_routes.router,
    codec_routes.router,
    profile_routes.router,
    series_routes.router,
    system_routes.router,
    websocket_routes.router
]

for router in routers:
    app.include_router(router)

# Mount directories
os.makedirs("../config", exist_ok=True)
app.mount("/config", StaticFiles(directory="config"), name="config")
app.mount("/static", StaticFiles(directory="frontend/build/static"), name="static")

# Start tasks


async def startup_event():
    asyncio.create_task(scan.scan_all_series())
    asyncio.create_task(scan_routes.scan_queue())
    asyncio.create_task(periodic.process_episodes_in_queue_periodic())
    asyncio.create_task(periodic.start_watchdog(await get_root_folder() + '/series'))
app.add_event_handler("startup", startup_event)

# Setup Logger


setup_logger()

# Catch all static routes


@app.get("/{full_path:path}")
async def read_item(request: Request, full_path: str):
    file_path = Path(f"frontend/build/{full_path}")
    if not file_path.exists() or file_path.is_dir():
        file_path = Path("frontend/build/index.html")

    if file_path.suffix in [".png", ".jpg", ".jpeg"]:
        return FileResponse(str(file_path), media_type="image/png")
    elif file_path.suffix == ".ico":
        return FileResponse(str(file_path), media_type="image/x-icon")
    else:
        return HTMLResponse(file_path.read_text(), media_type="text/html")
