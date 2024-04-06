from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import ForeignKey, Integer, String, DATETIME
from sqlalchemy.orm import relationship, mapped_column, Mapped

# check if this is neccessary
if TYPE_CHECKING:
    from .department import Department
    from .employee import Employee


class Employee(Base):
    __tablename__ = "hired_employees"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(255))
    datetime: Mapped[DATETIME] = mapped_column(DATETIME)
    department_id: Mapped[int] = mapped_column(Integer, ForeignKey("departments.id"))
    job_id: Mapped[int] = mapped_column(Integer, ForeignKey("jobs.id"))

