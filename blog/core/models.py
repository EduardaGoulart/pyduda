from django.db import models
from django.utils import timezone


class Preview(models.Model):
    author = models.CharField(max_length=250)
    resume = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    pushised_data = models.DateTimeField(blank=True, null=True)
    id_publish = models.IntegerField()

    def publish(self):
        self.pushised_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Tutorial(models.Model):
    id_publish = models.IntegerField()
    author = models.CharField(max_length=250)
    resume = models.TextField()
    title = models.CharField(max_length=250)
    pushised_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.id_publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class PreviewLife(models.Model):
    author = models.CharField(max_length=250)
    resume = models.CharField(max_length=500)
    title = models.CharField(max_length=100)
    pushised_data = models.DateTimeField(blank=True, null=True)
    id_publish = models.IntegerField()

    def publish(self):
        self.pushised_data = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class TutorialLife(models.Model):
    id_publish = models.IntegerField()
    author = models.CharField(max_length=250)
    resume = models.TextField()
    title = models.CharField(max_length=250)
    pushised_data = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.id_publish = timezone.now()
        self.save()

    def __str__(self):
        return self.title