import pytest
from projects.models import Project, Task

pytestmark = pytest.mark.django_db


def test_user_can_create_task_in_own_project(auth_client_a, user_a):
    project = Project.objects.create(owner=user_a, name="A1")

    res = auth_client_a.post(
        f"/api/projects/{project.id}/tasks/",
        {"title": "T1", "description": "", "status": "todo"},
        format="json",
    )
    assert res.status_code == 201
    assert res.data["project"] == project.id


def test_user_cannot_list_tasks_for_other_users_project(auth_client_a, user_a, user_b):
    project_b = Project.objects.create(owner=user_b, name="B1")
    Task.objects.create(project=project_b, title="B-task", status="todo")

    res = auth_client_a.get(f"/api/projects/{project_b.id}/tasks/")
    assert res.status_code == 404
