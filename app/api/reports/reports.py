import logging

from db.deps import get_ro_session
from fastapi import APIRouter, Depends
from fastapi_versioning import version
from schemas.reports import ReportEmployeeAboveAverageOutput, ReportEmployeeOutput
from services.reports import ReportsService
from sqlalchemy.orm import Session

router = APIRouter()

logger = logging.getLogger(f"app.{__name__}")


@router.get("/reports/employees_by_quarter")
@version(1, 0)
async def get_employees_report(year: int, session: Session = Depends(get_ro_session)) -> ReportEmployeeOutput:
    logger.info(f"Get employees report for year {year}")
    return ReportsService(session).get_employees_by_quarter(year)


@router.get("/reports/departments_above_average")
@version(1, 0)
async def get_departments_report(
    year: int, session: Session = Depends(get_ro_session)
) -> ReportEmployeeAboveAverageOutput:
    logger.info(f"Get departments report for year {year}")
    return ReportsService(session).get_above_average_hired_employees(year)
