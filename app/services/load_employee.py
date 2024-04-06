from models import Employee
from repositories.employee import EmployeeRepository
from sqlalchemy.orm import Session

class LoadEmployeeService:
    def __init__(self, session: Session) -> None:
        self.repository = EmployeeRepository(session)
    