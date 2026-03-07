from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime

class Task(SQLModel, table=True):
    __tablename__: str = "tasks"
    
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = Field(default=None, sa_type=String)
    description: str | None = Field(default=None, sa_type=String)
    is_completed: bool | None = False
    due_date: datetime | None = None
    create_at: datetime = Field(default_factory=datetime.now)
    