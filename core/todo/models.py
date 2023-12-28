from django.db import models

# Create your models here.

class Todo(models.Model):
    'create a model for todo app'
    
    title = models.CharField(max_length=245)
    body = models.TextField(default='', null=True, blank=True)
    done = models.BooleanField(default=False,)
    def __str__(self):
        return self.title
