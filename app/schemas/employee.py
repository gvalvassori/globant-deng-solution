import math
from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class EmployeeSchema(BaseModel):
    id: int | None = Field(..., description="Employee ID", examples=[1])
    name: str | None = Field(..., description="Employee Name", examples=["John Doe"])
    date_time: datetime | None = Field(
        ..., description="Date and Time of Hire", examples=["2021-09-01 09:00:00"]
    )
    department_id: int | None = Field(..., description="Department ID", examples=[1])
    job_id: int | None = Field(..., description="Job ID", examples=[1])

    @model_validator(mode="before")
    def validate_data(cls, v):
        if v["id"] is None or v["id"] < 0 or math.isnan(v["id"]):
            v["id"] = None
        if v["name"] is None or isinstance(v["name"], float):
            v["name"] = None
        if not isinstance(v["date_time"], datetime) and not isinstance(
            v["date_time"], float
        ):
            v["date_time"] = datetime.fromisoformat(v["date_time"])
        if isinstance(v["date_time"], float):
            v["date_time"] = None
        if (
            v["department_id"] is None
            or v["department_id"] < 0
            or math.isnan(v["department_id"])
        ):
            v["department_id"] = None
        if v["job_id"] is None or v["job_id"] < 0 or math.isnan(v["job_id"]):
            v["job_id"] = None
        return v


class EmployeeCSV(BaseModel):
    data: list[EmployeeSchema]
