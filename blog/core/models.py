from django.db import models
from django.utils import timezone


class Tutorial(models.Model):
    author = models.CharField(max_length=250)
    resume = models.TextField()
    title = models.CharField(max_length=100)
    pushised_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.pushised_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title
