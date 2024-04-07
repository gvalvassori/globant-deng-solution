import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from starlette.responses import Response

API_VERSION = "v1_0"
TEST_API_TOKEN = "Bearer test"


class BaseAPITest:
    client: TestClient

    def get(self, url: str) -> Response:
        return self.client.get(f"/{API_VERSION}/{url}")

    def post(self, url: str, json: dict) -> Response:
        return self.client.post(f"/{API_VERSION}/{url}", json=json)
