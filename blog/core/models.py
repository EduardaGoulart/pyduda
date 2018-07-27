from django.db import models


class Tutorial(models.Model):
    autor = models.CharField(max_length=250)
    texto = models.TextField()
    titulo = models.CharField(max_length=100)

    def __str__(self):
        return self.titulo
