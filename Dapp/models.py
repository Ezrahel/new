from tabnanny import verbose
from tkinter import CASCADE
from django.db import models

# Create your models here.
class Topic(models.Model):
    topicTitle = models.CharField(max_length=200)
    # body = models.TextField()
    dateAdded = models.DateTimeField(auto_now_add=True)

    """Attribute"""
    def __str__(self):
        return self.topicTitle

class record(models.Model):
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE)
    text = models.TextField()
    timeAdded = models.DateTimeField(auto_now_add=True)

    """The Meta class holds
    extra information for managing a model; here, it allows us to set a special
    attribute telling Django to use Entries when it needs to refer to more than
    one entry. Without this, Django would refer to multiple entries as Entrys.
    The __str__() method tells Django which information to show when it"""

    class Meta:
        verbose_name_plural = 'recordies'

    """Attribute
    Because an entry can be a long body of text,
    we tell Django to show just the
    first 50 characters of text"""
    def __str__(self):
            return f"{self.text[:50]}..."
