from fastapi import APIRouter

from src.services.todolist_service import TodoService
from src.dtos.todolist_dto import InsertTask, ReadTask, ListReadTask, UpdateTask
from src.deps.engine import db

router = APIRouter(prefix="/task", tags=["Tasks"])

@router.post("/", response_model=ReadTask, status_code=201)
def create_task(session: db, task_data: InsertTask) -> ReadTask:
    service = TodoService(session)
    task = service.create_task(task_data)
    return task

@router.get("/", response_model=ReadTask | ListReadTask, status_code=201)
def get_tasks(session: db, search_term: str | None = None) -> ReadTask | ListReadTask:
    service = TodoService(session)
    task = service.get_task(search_term)
    return task

@router.get("/{task_id}", response_model=ReadTask, status_code=201)
def get_task_by_id(session: db, task_id: int) -> ReadTask:
    service = TodoService(session)
    task = service.get_task_by_id(task_id)
    return task

@router.put("/{task_id}", response_model=ReadTask, status_code=200)
def update_task(session: db, task_id: int, data: UpdateTask) -> ReadTask:
    service = TodoService(session)
    task = service.update_task(data, task_id)
    return task