from models import Department
from repositories.department import DepartmentRepository
from sqlalchemy.orm import Session

class LoadDepartmentService:
    def __init__(self, session: Session) -> None:
        self.repository = DepartmentRepository(session)
    