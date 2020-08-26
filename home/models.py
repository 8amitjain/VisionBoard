from django.db import models
from django.utils import timezone


class ContactUs(models.Model):
    sender = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.sender
