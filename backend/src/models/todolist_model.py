from sqlmodel import SQLModel, Field
from sqlalchemy import String
from datetime import datetime, timezone

class Task(SQLModel, table=True):
    __tablename__: str = "tasks"
    
    id: int | None = Field(default=None, primary_key=True)
    title: str | None = Field(default=None, sa_type=String)
    description: str | None = Field(default=None, sa_type=String)
    is_completed: bool = Field(default=False)
    due_date: datetime | None = Field(default_factory=lambda: datetime.now(timezone.utc))
    create_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    