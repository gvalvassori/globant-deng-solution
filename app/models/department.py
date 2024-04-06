from db.base_class import Base
from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column, Mapped


class Department(Base):
    __tablename__ = "departments"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    department: Mapped[str] = mapped_column(String(255))

