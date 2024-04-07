from schemas.reports import ReportEmployee, ReportEmployeeAboveAverage
from sqlalchemy import text
from sqlalchemy.orm import Session


class ReportsService:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_employees_by_quarter(self, year: int) -> dict[str, list[ReportEmployee]]:
        """Get the number of employees hired by quarter for a given year.

        Args:
            year (int): The year to get the report for.

        Returns:
            dict[list[ReportEmployee]]: A dictionary containing the report data.
        """ """"""
        query = text(
            f"""
            SELECT
                d.department,
                j.job,
                SUM(CASE WHEN YEAR(h.datetime) = {year} AND QUARTER(h.datetime) = 1 THEN 1 ELSE 0 END) AS Q1,
                SUM(CASE WHEN YEAR(h.datetime) = {year} AND QUARTER(h.datetime) = 2 THEN 1 ELSE 0 END) AS Q2,
                SUM(CASE WHEN YEAR(h.datetime) = {year} AND QUARTER(h.datetime) = 3 THEN 1 ELSE 0 END) AS Q3,
                SUM(CASE WHEN YEAR(h.datetime) = {year} AND QUARTER(h.datetime) = 4 THEN 1 ELSE 0 END) AS Q4
            FROM hired_employees h
            JOIN departments d ON h.department_id = d.id
            JOIN jobs j ON h.job_id = j.id
            WHERE YEAR(h.datetime) = {year}
            GROUP BY d.department, j.job
            ORDER BY d.department, j.job;
            """
        )

        results = self.session.execute(query).mappings().all()
        return {"hired_employees_by_quarter": [ReportEmployee(**row) for row in results]}

    def get_above_average_hired_employees(self, year: int) -> dict[str, list[ReportEmployeeAboveAverage]]:
        """Get the departments that hired more employees than the average.

        Args:
            year (int): The year to get the report for.

        Returns:
            dict[list[ReportEmployeeAboveAverage]]: A dictionary containing the report data.
        """ """"""
        query = text(
            """
            SELECT
                d.id,
                d.department,
                COUNT(he.id) AS hired
            FROM hired_employees he
            JOIN departments d ON he.department_id = d.id
            WHERE he.datetime >= '2021-01-01' AND he.datetime < '2022-01-01'
            GROUP BY d.id, d.department
            HAVING COUNT(he.id) > (
                SELECT AVG(emp_count)
                FROM (
                    SELECT COUNT(id) AS emp_count
                    FROM hired_employees
                    WHERE datetime >= '2021-01-01' AND datetime < '2022-01-01'
                    GROUP BY department_id
                ) AS subquery
            )
            ORDER BY hired DESC;
        """
        )

        results = self.session.execute(query).mappings().all()
        return {"hired_employees_above_average": [ReportEmployeeAboveAverage(**row) for row in results]}
