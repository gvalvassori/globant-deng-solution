import logging

import pandas as pd
from db.deps import get_session
from fastapi import APIRouter, Depends, File, UploadFile
from fastapi_versioning import version
from services.load_department import LoadDepartmentService
from services.load_employee import LoadEmployeeService
from services.load_job import LoadJobService
from sqlalchemy.orm import Session
from starlette import status

router = APIRouter()

logger = logging.getLogger(f"app.{__name__}")


@router.post("/load/departments", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_departments(
    file: UploadFile = File(...), db: Session = Depends(get_session)
):
    reader = pd.read_csv(
        file.file,
        header=None,
        names=["id", "department"],
        chunksize=1000,
        iterator=True,
    )
    service = LoadDepartmentService(db)
    service.file_extension(file.filename.split(".")[-1])
    return service.load(reader)


@router.post("/load/employees", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_employees(
    file: UploadFile = File(...), db: Session = Depends(get_session)
):
    reader = pd.read_csv(
        file.file,
        header=None,
        names=["id", "name", "date_time", "department_id", "job_id"],
        chunksize=1000,
        iterator=True,
        keep_default_na=True,
    )
    service = LoadEmployeeService(db)
    service.file_extension(file.filename.split(".")[-1])
    return service.load(reader)


@router.post("/load/jobs", status_code=status.HTTP_201_CREATED)
@version(1, 0)
async def load_jobs(file: UploadFile = File(...), db: Session = Depends(get_session)):
    reader = pd.read_csv(
        file.file, header=None, names=["id", "job"], chunksize=1000, iterator=True
    )
    service = LoadJobService(db)
    service.file_extension(file.filename.split(".")[-1])
    return service.load(reader)
