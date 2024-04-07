from services.base import BaseService


class TestBaseService:
    def test_file_extension_valid_extension(self):
        session = None
        base_service = BaseService(session)
        extension = "csv"

        try:
            base_service.file_extension(extension)
        except ValueError:
            assert "Unexpected ValueError raised."

    def test_file_extension_invalid_extension(self):
        session = None
        base_service = BaseService(session)
        extension = "txt"

        try:
            base_service.file_extension(extension)
            assert "Expected ValueError not raised."
        except ValueError as e:
            assert str(e) == "Invalid file extension. Only CSV files are allowed."
