from pydantic import BaseModel, Field


class JobSchema(BaseModel):
    id: int = Field(..., description="Job ID", examples=1)
    job: str = Field(..., description="Job Title", examples="Software Engineer")

class JobCSV(BaseModel):
    data: list[JobSchema]