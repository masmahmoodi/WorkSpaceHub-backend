import pytest
from projects.models import Project

pytestmark = pytest.mark.django_db


def test_projects_list_requires_auth(api_client):
    res = api_client.get("/api/projects/")
    assert res.status_code == 401


def test_user_sees_only_their_projects(auth_client_a, user_a, user_b):
    Project.objects.create(owner=user_a, name="A1")
    Project.objects.create(owner=user_b, name="B1")

    res = auth_client_a.get("/api/projects/")
    assert res.status_code == 200
    assert res.data["count"] == 1
    assert res.data["results"][0]["name"] == "A1"


def test_user_cannot_retrieve_other_users_project(auth_client_a, user_a, user_b):
    other_project = Project.objects.create(owner=user_b, name="B1")

    res = auth_client_a.get(f"/api/projects/{other_project.id}/")
    assert res.status_code == 404


def test_user_can_create_project_owner_is_set(auth_client_a, user_a):
    res = auth_client_a.post("/api/projects/", {"name": "New", "description": ""}, format="json")
    assert res.status_code == 201
    assert res.data["owner"] == user_a.id
