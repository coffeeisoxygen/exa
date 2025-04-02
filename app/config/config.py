import configparser
import os


class AppConfig:
    def __init__(self, config_file="app.ini"):
        self.config_file = os.path.join(os.path.dirname(__file__), "../", config_file)
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        """Load the configuration file."""
        if not os.path.exists(self.config_file):
            self.create_default_config()
        self.config.read(self.config_file)

    def create_default_config(self):
        """Create a default configuration file if it doesn't exist."""
        self.config["path"] = {
            "adb_path": "/path/to/adb",
            "scrcpy_path": "/path/to/scrcpy",
        }
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)

    def get_path(self, key):
        """Get the path for a given key."""
        return self.config["path"].get(key, "")

    def set_path(self, key, value):
        """Set the path for a given key and save the configuration."""
        self.config["path"][key] = value
        with open(self.config_file, "w") as configfile:
            self.config.write(configfile)
