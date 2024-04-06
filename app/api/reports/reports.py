import logging

from db.deps import get_session
from fastapi import APIRouter, Depends
from fastapi_versioning import version
from services.reports import ReportsService
from sqlalchemy.orm import Session

router = APIRouter()

logger = logging.getLogger(f"app.{__name__}")


@router.get("/reports/employees")
@version(1, 0)
async def get_employees_report(session: Session = Depends(get_session)):
    service = ReportsService(session)
    return service.get_employees_report()


@router.get("/reports/departments")
@version(1, 0)
async def get_departments_report(session: Session = Depends(get_session)):
    service = ReportsService(session)
    return service.get_departments_report()
