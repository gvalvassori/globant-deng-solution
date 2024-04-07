from pydantic import BaseModel

class ReportEmployee(BaseModel):
    department: str
    job: str
    Q1: int
    Q2: int
    Q3: int
    Q4: int

class ReportEmployeeOutput(BaseModel):
    hired_employees_by_quarter: list[ReportEmployee]

class ReportEmployeeAboveAverage(BaseModel):
    id: int
    department: str
    hired: int

class ReportEmployeeAboveAverageOutput(BaseModel):
    hired_employees_above_average: list[ReportEmployeeAboveAverage]