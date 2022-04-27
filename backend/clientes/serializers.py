from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cliente
        fields=["Nombres","Apellidos","Fecha_de_nacimiento","Genero","Numero_de_contacto","Correo_electronico"]