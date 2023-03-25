from django.db import models

# Create your models here.

class Project(models.Model):
    project_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.project_id
    

