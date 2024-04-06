from models import Department
from repositories.base import ModelRepository


class DepartmentRepository(ModelRepository):
    model = Department
