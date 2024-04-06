from models import Job
from repositories.job import JobRepository
from sqlalchemy.orm import Session

class LoadJobService:
    def __init__(self, session: Session) -> None:
        self.repository = JobRepository(session)
    