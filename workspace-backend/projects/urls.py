from django.urls import path
from .views import ProjectListCreateView, ProjectRetrieveUpdateDestroy, TaskListCreateView, TaskDetailView
urlpatterns = [
   path("projects/", ProjectListCreateView.as_view(), name="list_create_projects"),
   path("projects/<int:pk>/",  ProjectRetrieveUpdateDestroy.as_view(), name="project_details" ),
   path("projects/<int:project_id>/tasks/",TaskListCreateView.as_view(), name="list_create_projects"),
   path("projects/<int:project_id>/tasks/<int:pk>/",TaskDetailView.as_view(), name="tasks_details"),


   
]
