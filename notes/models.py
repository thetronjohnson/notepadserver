from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=255)
    note = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title