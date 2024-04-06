from pydantic import BaseModel, Field
from datetime import datetime

class EmployeeSchema(BaseModel):
    id: int = Field(..., description="Employee ID", examples=1)
    name: str = Field(..., description="Employee Name", examples="John Doe")
    date_time: datetime = Field(..., description="Date and Time of Hire", examples="2021-09-01 09:00:00")
    department_id: int = Field(..., description="Department ID", examples=1)
    job_id: int = Field(..., description="Job ID", examples=1)

class EmployeeCSV(BaseModel):
    data: list[EmployeeSchema]