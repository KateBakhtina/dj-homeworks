import pytest
import random
from django.shortcuts import reverse

from .fixtures import api_client, courses_factory
from students.models import Course


@pytest.mark.django_db
def test_courses_get_first_course(api_client, courses_factory):
    course = courses_factory()
    url = reverse("courses-detail", kwargs={"pk": course.id})

    assert Course.objects.count() == 1

    response = api_client.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data.get("name") == course.name


@pytest.mark.django_db
def test_courses_get(api_client, courses_factory):
    courses = courses_factory(_quantity=3)
    url = reverse("courses-list")

    response = api_client.get(url)

    assert response.status_code == 200
    assert Course.objects.count() == len(courses)


@pytest.mark.django_db
def test_courses_get_by_id(api_client, courses_factory):
    course = courses_factory()

    url = reverse("courses-detail", kwargs={"pk": course.id})
    response = api_client.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == course.id


@pytest.mark.django_db
def test_courses_filter_by_name(api_client, courses_factory):
    course = courses_factory()

    url = reverse("courses-list")
    response = api_client.get(url, data={"name": course.name})
    assert response.status_code == 200

    data = response.json()
    for object in data:
        assert object["name"] == course.name


@pytest.mark.django_db
def test_courses_post(api_client):

    url = reverse("courses-list")
    response = api_client.post(url, data={"name": "Курс 1"})
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == Course.objects.get(pk=data["id"]).name


@pytest.mark.django_db
def test_courses_patch(api_client, courses_factory):
    course = courses_factory()

    url = reverse("courses-detail", kwargs={"pk": course.id})

    response = api_client.patch(url, data={"name": "Курс 2"})
    assert response.status_code == 200

    data = response.json()
    assert data["name"] == Course.objects.get(pk=course.id).name


@pytest.mark.django_db
def test_courses_destroy(api_client, courses_factory):
    courses = courses_factory(_quantity=5)
    length_after_destroy = len(courses) - 1
    course = random.choice(courses)
    url = reverse("courses-detail", kwargs={"pk": course.id})

    response = api_client.delete(url)
    assert response.status_code == 204
    assert length_after_destroy == Course.objects.count()


@pytest.mark.parametrize(
    ["value"],
    (
            (20,),
            (19,),
            (21,),
    )
)
@pytest.mark.django_db
def test_courses_validate_count_students(value, settings):

    assert value <= settings.MAX_STUDENTS_PER_COURSE









