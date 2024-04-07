from pydantic import BaseModel, Field


class DepartmentSchema(BaseModel):
    id: int = Field(..., description="Department ID", examples=[1])
    department: str = Field(..., description="Department Name", examples=["Engineering"])


class DepartmentCSV(BaseModel):
    data: list[DepartmentSchema]
