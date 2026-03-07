from pydantic import BaseModel
from datetime import datetime

class InsertTask(BaseModel):
    title: str
    description: str | None = None
    is_completed: bool | None = False
    due_date: datetime | None = None
    
class ReadTask(BaseModel):
    id: int | None
    title: str 
    description: str | None
    is_completed: bool | None
    due_date: datetime | None
    created_at: datetime | None
    
class UpdateTask(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = False
    due_date: datetime | None = None

class ListReadTask(BaseModel):
    tasks: list[ReadTask]