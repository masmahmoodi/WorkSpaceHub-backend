import pytest
from projects.models import Project, Task

pytestmark = pytest.mark.django_db


def test_projects_search(auth_client_a, user_a):
    Project.objects.create(owner=user_a, name="Alpha", description="hello world")
    Project.objects.create(owner=user_a, name="Beta", description="nothing")

    res = auth_client_a.get("/api/projects/?search=hello")
    assert res.status_code == 200
    assert res.data["count"] == 1
    assert res.data["results"][0]["name"] == "Alpha"


def test_projects_filter_by_name(auth_client_a, user_a):
    Project.objects.create(owner=user_a, name="One", description="")
    Project.objects.create(owner=user_a, name="Two", description="")

    res = auth_client_a.get("/api/projects/?name=Two")
    assert res.status_code == 200
    assert res.data["count"] == 1
    assert res.data["results"][0]["name"] == "Two"


def test_tasks_filter_by_status(auth_client_a, user_a):
    project = Project.objects.create(owner=user_a, name="P1")
    Task.objects.create(project=project, title="T1", status="todo")
    Task.objects.create(project=project, title="T2", status="done")

    res = auth_client_a.get(f"/api/projects/{project.id}/tasks/?status=done")
    assert res.status_code == 200
    assert len(res.data["results"]) == 1
    assert res.data["results"][0]["title"] == "T2"


def test_tasks_search(auth_client_a, user_a):
    project = Project.objects.create(owner=user_a, name="P1")
    Task.objects.create(project=project, title="Pay rent", description="urgent", status="todo")
    Task.objects.create(project=project, title="Gym", description="", status="todo")

    res = auth_client_a.get(f"/api/projects/{project.id}/tasks/?search=rent")
    assert res.status_code == 200
    assert len(res.data["results"]) == 1
    assert res.data["results"][0]["title"] == "Pay rent"
