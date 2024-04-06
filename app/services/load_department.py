import itertools

import pandas as pd
from models import Department
from repositories.department import DepartmentRepository
from schemas.department import DepartmentCSV, DepartmentSchema
from services.base import BaseService
from sqlalchemy.orm import Session


class LoadDepartmentService(BaseService):
    def __init__(self, session: Session) -> None:
        self.repository = DepartmentRepository(session)

    def _et(self, reader: pd.io.parsers.readers.TextFileReader) -> DepartmentCSV:
        """Extract and transform the data into a DepartmentCSV object.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be transformed.

        Returns:
            DepartmentCSV: A DepartmentCSV object.
        """
        reader1, reader2 = itertools.tee(reader)
        self.validate_data(reader1, 2)
        data = DepartmentCSV(data=[])

        for chunk in reader2:
            for _, row in chunk.iterrows():
                department = DepartmentSchema(
                    id=row["id"],
                    department=row["department"],
                )
                data.data.append(department)
        return data

    def load(
        self, reader: pd.io.parsers.readers.TextFileReader
    ) -> DepartmentRepository.model:
        """Load the data into the database.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be loaded.

        Returns:
            DepartmentRepository.model: A list of Department instances.
        """
        data = self._et(reader)
        department_instances = []
        for d in data.data:
            instance = Department(
                id=d.id,
                department=d.department,
            )
            department_instances.append(instance)

        return self.repository.bulk_insert(department_instances)
