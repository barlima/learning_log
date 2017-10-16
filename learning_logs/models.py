from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Topic which a user is currently up to"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Returns string representation of a model"""
        return self.text


class Entry(models.Model):
    """Info about the study progress"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Returns string representation of an Entry"""
        if len(self.text) > 50:
            return self.text[0:50] + "..."
        return self.text

