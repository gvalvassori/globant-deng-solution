import itertools

import pandas as pd
from models import Employee
from repositories.employee import EmployeeRepository
from schemas.employee import EmployeeCSV, EmployeeSchema
from services.base import BaseService
from sqlalchemy.orm import Session


class LoadEmployeeService(BaseService):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.repository = EmployeeRepository(session)

    def _et(self, reader: pd.io.parsers.readers.TextFileReader) -> EmployeeCSV:
        """Extract and transform the data into a EmployeeCSV object.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be transformed.

        Returns:
            EmployeeCSV: A EmployeeCSV object.
        """
        reader1, reader2 = itertools.tee(reader)
        self.validate_data(reader1, 5)
        data = EmployeeCSV(data=[])

        for chunk in reader2:
            for _, row in chunk.iterrows():
                employee = EmployeeSchema(
                    id=row["id"],
                    name=row["name"],
                    date_time=row["date_time"],
                    department_id=row["department_id"],
                    job_id=row["job_id"],
                )
                data.data.append(employee)
        return data

    def load(
        self, reader: pd.io.parsers.readers.TextFileReader
    ) -> EmployeeRepository.model:
        """Load the data into the database.

        Args:
            reader (pd.io.parsers.readers.TextFileReader): Dataframe to be loaded.

        Returns:
            EmployeeRepository.model: A list of Employee instances.
        """
        data = self._et(reader)
        employee_instances = []
        for d in data.data:
            instance = Employee(
                id=d.id,
                name=d.name,
                datetime=d.date_time,
                department_id=d.department_id,
                job_id=d.job_id,
            )
            employee_instances.append(instance)

        return self.repository.bulk_insert(employee_instances)
