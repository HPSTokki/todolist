from pathlib import Path

from sqlmodel import Session, create_engine, false
from fastapi import Depends
from typing import Generator, Annotated

BASE_PATH = Path(__file__).resolve().parent.parent.parent
LOCAL_DB_PATH = BASE_PATH / "local.db"

sqlite_url = "sqlite:///local.db"
connect_args = { "check_same_thread": false }

engine = create_engine(sqlite_url, connect_args=connect_args)

def get_engine() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
        
db = Annotated[Session, Depends(get_engine)]