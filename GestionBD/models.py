from django.db import models

# Create your models here.

class Entreprise(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False)
    localisation = models.CharField(max_length=50, blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Employe(models.Model):
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE)

    name = models.CharField(max_length=30, null=True)
    fonction = models.CharField(max_length=50, null=False, blank=False)
    salaire = models.FloatField()
    email = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

