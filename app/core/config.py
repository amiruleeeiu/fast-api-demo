import os

class Settings:
    UPLOAD_DIR = os.path.join(os.path.dirname(__file__), "..", "uploads")

settings = Settings()
