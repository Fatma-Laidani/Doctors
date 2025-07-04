from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    bio = models.TextField()
    photo = models.ImageField(upload_to='doctors/')

    def __str__(self):
        return self.name
