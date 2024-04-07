from schemas.department import DepartmentSchema


class TestDepartmentSchema:
    def test_instantiation_with_valid_values(self):
        department = DepartmentSchema(id=1, department="Engineering")
        assert department.id == 1
        assert department.department == "Engineering"
