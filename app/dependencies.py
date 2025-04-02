import os
import sys

from app.logging import logger
from app.models.base import Base, engine


def initialize_database():
    """Create all database tables if they don't exist"""
    try:
        logger.info("Initializing database...")
        Base.metadata.create_all(bind=engine)
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization failed: {e}")
        raise


def check_dependencies(config):
    """
    Check if adb.exe and scrcpy.exe exist in the configured paths.
    If not, prompt the user to provide the correct paths.
    """
    adb_path = config.get_path("adb_path")
    scrcpy_path = config.get_path("scrcpy_path")

    if not os.path.isfile(adb_path) or not os.path.isfile(scrcpy_path):
        print("Dependencies not found!")
        print("Please provide the correct paths for adb.exe and scrcpy.exe.")

        # Prompt user for paths
        adb_path = input("Enter the full path to adb.exe: ").strip()
        scrcpy_path = input("Enter the full path to scrcpy.exe: ").strip()

        # Validate paths
        if not os.path.isfile(adb_path):
            print(f"Invalid path for adb.exe: {adb_path}")
            sys.exit(1)
        if not os.path.isfile(scrcpy_path):
            print(f"Invalid path for scrcpy.exe: {scrcpy_path}")
            sys.exit(1)

        # Update config
        config.set_path("adb_path", adb_path)
        config.set_path("scrcpy_path", scrcpy_path)

        print("Paths updated successfully. Restarting the application...")
        os.execv(sys.executable, [sys.executable] + sys.argv)

    logger.info("Dependencies check passed successfully")
