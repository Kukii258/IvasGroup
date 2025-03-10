import os

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.

class Slika(models.Model):

    CATEGORY_CHOICES = (
        ('corporate', 'Corporate Events'),
        ('concert', 'Concert and Touring'),
        ('sport', 'Sporting Events'),
        ('ambition', 'Exhibitions'),
        ('broadcast', 'TV Broadcasting'),
    )

    naslov = models.CharField(max_length=100, null=True, blank=True)
    podnaslov = models.CharField(max_length=100, null=True, blank=True)
    slika = models.ImageField(upload_to='album', null=True, blank=True)

    sirina = models.IntegerField(default=1500)
    visina = models.IntegerField(default=1000)

    kategorija = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)

    datum_uploada = models.DateTimeField(auto_now_add=True,blank=True,null=True)


    def clean(self):

        if not self.slika:
            raise ValidationError("Moraš uplodat-i sliku.")


    def __str__(self):
        if self.naslov:
            return f" {self.naslov} - {self.datum_uploada.strftime('%d. %m. %Y')}"
        else:
            naslov_slike = os.path.splitext(os.path.basename(self.slika.name))[0]  # Extracts 'zenska4'
            return f"{naslov_slike} - {self.datum_uploada.strftime('%d. %m. %Y')}"
