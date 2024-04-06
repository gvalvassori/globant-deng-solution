from db.base_class import Base
from sqlalchemy import DATETIME, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class Employee(Base):
    __tablename__ = "hired_employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255), nullable=True)
    datetime: Mapped[DATETIME] = mapped_column(DATETIME, nullable=True)
    department_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("departments.id"), nullable=True
    )
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey("jobs.id"), nullable=True)
