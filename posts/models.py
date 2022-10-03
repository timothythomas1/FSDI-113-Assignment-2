
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
class Archived(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name
class Published(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE # When deleting, everything related to it gets deleted
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        blank=True, # This allows the status field be null for existing records.
        null=True   # This allows the status field be null for existing records.
    )
    archived = models.ForeignKey(
        Archived,
        on_delete=models.CASCADE,
        blank=True, # This allows the status field be null for existing records.
        null=True   # This allows the status field be null for existing records.
    ) 
    published = models.ForeignKey(
        Published,
        on_delete=models.CASCADE,
        blank=True, # This allows the status field be null for existing records.
        null=True   # This allows the status field be null for existing records.
    ) 

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])


