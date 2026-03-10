from typing import cast

from sqlmodel import Session, col, select
from src.exception import TaskDoesNotExists
from src.models.todolist_model import Task
from src.dtos.todolist_dto import InsertTask, ReadTask, UpdateTask, ListReadTask

class TodoService():
    def __init__(self, session: Session) -> None:
        self.session = session
     
    def create_task(self, task_data: InsertTask) -> ReadTask:
        task = Task(**task_data.model_dump())
        self.session.add(Task)
        self.session.commit()
        self.session.refresh(Task)
        return ReadTask.model_validate(task)
    
    def get_task(self, search_term: str | None = None) -> ReadTask | ListReadTask:
        if search_term:
            task = self.session.exec(
                select(Task).where(col(Task.title).ilike(f"{search_term}"))
            ).first()
            if not task:
                raise TaskDoesNotExists()
            return cast(ReadTask, task)
        tasks = self.session.exec(select(Task)).all()
        validated_task = [ReadTask.model_validate(a) for a in tasks]
        return ListReadTask(tasks=validated_task)
    
    def get_task_by_id(self, task_id: int) -> ReadTask:
        task = self.session.get(Task, task_id)
        return ReadTask.model_validate(task)
    
    def update_task(self, update_data: UpdateTask, task_id: int) -> ReadTask:
        updated_task = self.session.get(Task, task_id)
        if not updated_task:
            raise TaskDoesNotExists()
        for key, value in update_data.model_dump(exclude_unset=True).items():
            setattr(updated_task, key, value)
        self.session.commit()
        self.session.refresh(updated_task)
        return ReadTask.model_validate(updated_task)
    
    def delete_task(self, task_id: int) -> ReadTask:
        task = self.session.get(Task, task_id)
        if not task:
            raise TaskDoesNotExists()
        self.session.delete(task)
        self.session.commit()
        return ReadTask.model_validate(task)