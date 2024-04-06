import itertools

import pandas as pd
from models import Job
from repositories.job import JobRepository
from schemas.job import JobCSV, JobSchema
from services.base import BaseService
from sqlalchemy.orm import Session


class LoadJobService(BaseService):
    def __init__(self, session: Session) -> None:
        self.repository = JobRepository(session)

    def _et(self, reader: pd.io.parsers.readers.TextFileReader) -> JobCSV:
        """Extract and transform the data into a JobCSV object.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be transformed.

        Returns:
            JobCSV: A JobCSV object.
        """
        reader1, reader2 = itertools.tee(reader)
        self.validate_data(reader1, 2)
        data = JobCSV(data=[])

        for chunk in reader2:
            for _, row in chunk.iterrows():
                job = JobSchema(
                    id=row["id"],
                    job=row["job"],
                )
                data.data.append(job)
        return data

    def load(self, reader: pd.io.parsers.readers.TextFileReader) -> JobRepository.model:
        """Load the data into the database.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be loaded.

        Returns:
            JobRepository.model: A list of Job instances.
        """
        data = self._et(reader)
        job_instances = []
        for d in data.data:
            instance = Job(
                id=d.id,
                job=d.job,
            )
            job_instances.append(instance)

        return self.repository.bulk_insert(job_instances)
