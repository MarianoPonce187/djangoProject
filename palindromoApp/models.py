from django.db import models

# Create your models here.
class Palabra(models.Model):
    palabra = models.CharField(max_length=255, unique=True)
    es_palindromo = models.BooleanField(default=False)
    fecha_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.palabra