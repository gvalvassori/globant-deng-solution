from db.base_class import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped

class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    job: Mapped[str] = mapped_column(String(255))