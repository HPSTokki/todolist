from fastapi import HTTPException, status

class DomainException(Exception):
    def __init__(self, status_code: int, message: str) -> None:
        self.status_code = status_code
        self.message = message
        
class TaskDoesNotExists(DomainException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND, 
            message="Task not found"
        )