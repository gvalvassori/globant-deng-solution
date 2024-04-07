from datetime import datetime

from schemas.employee import EmployeeSchema


class TestEmployeeSchema:
    def test_valid_input_values(self):
        employee = EmployeeSchema(
            id=1, name="John Doe", date_time=datetime(2021, 9, 1, 9, 0, 0), department_id=1, job_id=1
        )
        assert employee.id == 1
        assert employee.name == "John Doe"
        assert employee.date_time == datetime(2021, 9, 1, 9, 0, 0)
        assert employee.department_id == 1
        assert employee.job_id == 1
