import pytest
import random

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):
    """проверка получения первого курса"""
    courses = course_factory(_quantity=1)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_get_list_course(client, course_factory):
    """проверка получения списка курсов"""
    courses = course_factory(_quantity=10)
    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)


@pytest.mark.django_db
def test_id_filter_course(client, course_factory):
    """проверка фильтрации списка курсов по id"""
    courses = course_factory(_quantity=10)
    course_id = random.choice(courses).id
    response = client.get("/api/v1/courses/", {"id": course_id})
    data = response.json()
    assert response.status_code == 200
    assert data[0]['id'] == course_id
    assert 'id' and 'name' and 'students' in data[0]


@pytest.mark.django_db
def test_name_filter_course(client, course_factory):
    """проверка фильтрации списка курсов по name"""
    courses = course_factory(_quantity=10)
    course_name = random.choice(courses).name
    response = client.get("/api/v1/courses/", {"name": course_name})
    data = response.json()
    assert response.status_code == 200
    assert data[0]['name'] == course_name
    assert 'id' and 'name' and 'students' in data[0]


@pytest.mark.django_db
def test_create_course(client):
    """тест успешного создания курса"""
    response = client.post("/api/v1/courses/", {'name': 'Unique_course'})
    data = response.json()
    assert response.status_code == 201
    assert data['name'] == 'Unique_course'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    """тест успешного обновления курса"""
    courses = course_factory(_quantity=10)
    course_id = random.choice(courses).id
    response = client.patch(path=f"/api/v1/courses/{course_id}/", data={"name": "Unique_course"})
    data = response.json()
    assert response.status_code == 200
    assert data['name'] == 'Unique_course'
    assert 'Unique_course' not in courses
    assert 'Unique_course' in data['name']


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    """тест успешного удаления курса"""
    courses = course_factory(_quantity=10)
    course_id = random.choice(courses).id
    response = client.delete(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 204
    assert Course.objects.count() == 9


@pytest.fixture
def specific_settings(settings):
    max_students = settings.MAX_STUDENTS_PER_COURSE
    return max_students


@pytest.mark.parametrize(
    ['quantity', 'expected'],
    ((20, True), (10, False), (30, False))
)
def test_queries_students(specific_settings, quantity, expected):
    """проверка валидации на макс.количество студентов на курсе"""
    result = quantity == specific_settings
    assert result == expected
