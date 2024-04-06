import logging

from db.deps import get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import version
from schemas import DepartmentSchema, DepartmentCSV, EmployeeSchema, EmployeeCSV, JobSchema, JobCSV
from services.load_department import LoadDepartmentService
from services.load_employee import LoadEmployeeService
from services.load_job import LoadJobService
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter()

logger = logging.getLogger(f"app.{__name__}")

@router.post("/load/departments", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_departments():
    pass

@router.post("/load/employees", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_employees():
    pass

@router.post("/load/jobs", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_jobs():
    pass
