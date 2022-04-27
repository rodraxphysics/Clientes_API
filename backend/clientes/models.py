from django.db import models

# Create your models here.

class Cliente(models.Model):
    Nombres=models.CharField(max_length=24,null=False)
    Apellidos=models.CharField(max_length=24,null=False)
    Fecha_de_nacimiento=models.DateField(null=False)
    Genero=models.CharField(max_length=9,null=False)
    Numero_de_contacto=models.PositiveIntegerField(null=False,default=9999999999)
    Correo_electronico=models.EmailField(null=False,default="email@test.com")