from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.config.config import AppConfig
from app.dependencies import check_dependencies, initialize_database
from app.logging import logger


def create_app():
    # Initialize FastAPI app
    app = FastAPI(
        title="Android Device Control",
        description="Application for controlling Android devices and GSM modems",
        version="0.1.0",
    )

    # Mount static files
    app.mount(
        "/static",
        StaticFiles(directory=Path(__file__).parent / "static"),
        name="static",
    )

    # Setup templates
    templates = Jinja2Templates(directory=Path(__file__).parent / "templates")

    # Register routes here (will be implemented later)
    # from app.routes import device_routes, modem_routes
    # app.include_router(device_routes.router)
    # app.include_router(modem_routes.router)

    return app


def main():
    # Load configuration
    config = AppConfig()

    # Check dependencies
    check_dependencies(config)

    # Initialize database
    initialize_database()

    # Start the application
    logger.info("Starting the FastAPI application...")

    # Create the FastAPI app
    app = create_app()

    # Run the server
    uvicorn.run(
        "app.main:create_app", host="0.0.0.0", port=8000, reload=True, factory=True
    )


if __name__ == "__main__":
    main()
