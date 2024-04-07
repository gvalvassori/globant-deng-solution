from schemas.reports import ReportEmployee, ReportEmployeeAboveAverage


class TestReportsSchema:
    def test_valid_report_employee(self):
        department = "Sales"
        job = "Manager"
        q1 = 10
        q2 = 15
        q3 = 20
        q4 = 25

        report_employee = ReportEmployee(department=department, job=job, Q1=q1, Q2=q2, Q3=q3, Q4=q4)

        assert report_employee.department == department
        assert report_employee.job == job
        assert report_employee.Q1 == q1
        assert report_employee.Q2 == q2
        assert report_employee.Q3 == q3
        assert report_employee.Q4 == q4

    def test_create_report_employee_above_average_valid_values(self):
        id = 1
        department = "Sales"
        hired = 10

        report_employee_above_average = ReportEmployeeAboveAverage(id=id, department=department, hired=hired)

        assert report_employee_above_average.id == id
        assert report_employee_above_average.department == department
        assert report_employee_above_average.hired == hired
