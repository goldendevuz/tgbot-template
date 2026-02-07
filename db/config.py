from dotenv import load_dotenv
import os

from utils.config import CF as conf
from utils.path import ENV_PATH

load_dotenv(ENV_PATH)


class Config:
    # 1️⃣ Agar DB_URL bo'lsa — faqat shuni ishlat
    DB_URL = os.getenv("DB_URL")

    if DB_URL:
        DB_CONFIG = DB_URL.strip()
    else:
        DB_USER = conf.db.DB_USER
        DB_PASSWORD = conf.db.DB_PASSWORD
        DB_NAME = conf.db.DB_NAME
        DB_HOST = conf.db.DB_HOST
        DB_PORT = conf.db.DB_PORT

        # 2️⃣ Port faqat mavjud bo'lsa qo‘shiladi
        if DB_PORT and str(DB_PORT).lower() != "none":
            host = f"{DB_HOST}:{int(DB_PORT)}"
        else:
            host = DB_HOST

        DB_CONFIG = (
            f"postgresql+asyncpg://"
            f"{DB_USER}:{DB_PASSWORD}@{host}/{DB_NAME}"
        )
