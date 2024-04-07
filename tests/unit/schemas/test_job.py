from schemas.job import JobSchema


class TestJobSchema:
    def test_valid_job_schema_object(self):
        job_schema = JobSchema(id=1, job="Software Engineer")
        assert job_schema.id == 1
        assert job_schema.job == "Software Engineer"
