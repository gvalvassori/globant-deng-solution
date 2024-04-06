from models import Employee
from repositories.base import ModelRepository


class EmployeeRepository(ModelRepository):
    model = Employee
