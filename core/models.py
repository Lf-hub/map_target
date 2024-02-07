from django.db import models

# Create your models here.


class Target(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    latitude = models.FloatField(verbose_name='Latitude', null=True, blank=True)
    longitude = models.FloatField(verbose_name='Longitude', null=True, blank=True)
    expiration_date = models.DateField(verbose_name='Data de expiração', null=True, blank=True)
   
    class Meta:
        verbose_name = 'Alvo'
        verbose_name_plural = 'Alvos'
    
    def __str__(self):
        return self.name
    