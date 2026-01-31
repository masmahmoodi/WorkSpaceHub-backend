from .serializers import ProjectSerializer, TaskSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Project,Task
from rest_framework.permissions import IsAuthenticated
from .permissions import IsProjectOwner, IsTaskProjectOwner


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from django.shortcuts import get_object_or_404
#  projects list and create view
class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["name"]
    search_fields = ["name", "description"]
    ordering_fields = ["created_at", "updated_at"]
    ordering = ["-created_at"]




    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    #  create a project 
    def perform_create(self,serializer):
        return serializer.save(owner=self.request.user)


class ProjectRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsProjectOwner]
    serializer_class = ProjectSerializer

    # show data to authorized users
    def get_queryset(self):
        return Project.objects.filter(owner=self.request.user)
    


class TaskListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer


    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status"]
    search_fields = ["title", "description"]
    ordering_fields = ["created_at", "updated_at", "status"]
    ordering = ["-created_at"]


    def get_project(self):
        return get_object_or_404(
            Project,
            id=self.kwargs["project_id"],
            owner=self.request.user,
        )

    

    def perform_create(self,serializer):
        project = self.get_project()

        return serializer.save(project=project)
    
    def  get_queryset(self):
        project = self.get_project()
        return Task.objects.filter(project=project)
    

class TaskDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsTaskProjectOwner]
    serializer_class = TaskSerializer

   

    def get_queryset(self):
        project = get_object_or_404(Project,id=self.kwargs["project_id"], owner=self.request.user)
        return Task.objects.filter(project=project)
