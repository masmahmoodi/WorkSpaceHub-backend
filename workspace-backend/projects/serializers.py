from rest_framework import serializers
from .models import Project, Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ("id","owner","name","description","created_at","updated_at")
        read_only_fields = ("id","owner")


class TaskSerializer(serializers.ModelSerializer):
    class  Meta:
        model = Task
        fields = ("id","project","title","description","status","created_at","updated_at")
        read_only_fields = ("id","project")
        