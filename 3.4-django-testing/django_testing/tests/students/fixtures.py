import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory