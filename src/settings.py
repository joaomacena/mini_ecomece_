from typing import Optional
from pathlib import Path
from pydantic import BaseSettings

DB_PATH = Path(__file__).resolve().parent


class Settings(BaseSettings):
    db_username: Optional[str] = None
    db_password: Optional[str] = None
    db_name: Optional[str] = None
    db_port: Optional[int] = None

    @property
    def db_url(self):
        return f'postgresql://{self.db_username}:{self.db_password}@db:{self.db_port}/{self.db_name}'
        #return f'sqlite:///{DB_PATH}/database.db'
    # 'sqlite:////C:/Acerela_python/mini_ecomerce_clean/src/database.db'


settings = Settings()
