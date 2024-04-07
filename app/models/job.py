from typing import TYPE_CHECKING

from db.base_class import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .employee import Employee


class Job(Base):
    __tablename__ = "jobs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    job: Mapped[str] = mapped_column(String(255))

    employee: Mapped["Employee"] = relationship("Employee", back_populates="job")
