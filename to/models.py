from django.db import models
from taggit.managers import TaggableManager

# Create your models here.

tasks = [
    ('OPEN', 'OPEN'),
    ('WORKING', 'WORKING'),
    ('DONE', 'DONE'),
    ('OVERDUE', 'OVERDUE'),
]


class Todo(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=1000, blank=False)
    tag = TaggableManager(blank=True)
    status = models.CharField(
        max_length=20, blank=False, choices=tasks, default='OPEN')
    due_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
