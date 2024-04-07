import logging

from api.router import api_router
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi_exceptionshandler import APIExceptionHandler, APIExceptionMiddleware
from fastapi_versioning import VersionedFastAPI
from middlewares.logging_middleware import LoggingMiddleware
from pydantic import ValidationError
from settings.project_settings import project_settings
from starlette.middleware.cors import CORSMiddleware
from starlette_context import plugins
from starlette_context.middleware import RawContextMiddleware

app = FastAPI(
    title="ETL and Reports",
    description="Load csv files, perform ETL and generate reports.",
    root_path=project_settings.RootPath,
)


# ==== Version
app = VersionedFastAPI(app, root_path=project_settings.RootPath)

# ==== Include internal routes
app.include_router(api_router, prefix="/api")

# ==== Logging
logger = logging.getLogger("app")
logger.addHandler(logging.StreamHandler())

# ==== Middlewares
app.add_middleware(LoggingMiddleware, logger_name="app.requests")
app.add_middleware(
    APIExceptionMiddleware,
    capture_unhandled=True,
    log_error=True,
    logger_name="app.exceptions",
)
app.add_middleware(RawContextMiddleware, plugins=(plugins.RequestIdPlugin(),))
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==== Exception handlers
if not project_settings.DEBUG:
    logger.setLevel(logging.INFO)
    app.add_exception_handler(RequestValidationError, APIExceptionHandler.unhandled)
    app.add_exception_handler(ValidationError, APIExceptionHandler.unhandled)
else:
    logger.setLevel(logging.DEBUG)
