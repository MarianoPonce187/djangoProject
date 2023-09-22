from django.db import models

# Create your models here.
class Palindromo(models.Model):
    palabra = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    check_palindromo = models.BooleanField(default=False)

    def __str__(self):
        return self.palabra