from api.load import load_csv
from api.reports import reports
from fastapi import APIRouter

api_router = APIRouter()

# Load CSV
api_router.include_router(load_csv.router, tags=["Load CSV"])

# Reports
api_router.include_router(reports.router, tags=["Reports"])