from django.db import models
from django.conf import settings
# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="projects")
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    

class Task(models.Model):
    class Status(models.TextChoices):
        TODO = "todo","To Do"
        IN_PROGRESS = "in_progress", "In Progress"
        DONE = "done", "Done"


    title = models.CharField(max_length=200)
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name="tasks")
    description = models.TextField(blank=True)
    status = models.CharField(max_length=30,choices=Status.choices,default=Status.TODO)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    


