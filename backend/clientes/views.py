from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Cliente
from .serializers import ClienteSerializer
from rest_framework import generics,mixins

# Create your views here.
class ClienteMixinView(mixins.CreateModelMixin,mixins.ListModelMixin,mixins.RetrieveModelMixin,generics.GenericAPIView):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer
    lookup_field="pk"

    def get(self,request,*args,**kwargs):
        pk=kwargs.get("pk")
        if pk is not None:
            return self.retrieve (request,*args,**kwargs)
        return self.list(request,*args,*kwargs)

    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def perform_create(self,serializer):
        Nombres=serializer.validated_data.get("Nombres")
        Apellidos=serializer.validated_data.get("Apellidos")
        Fecha_de_nacimiento=serializer.validated_data.get("Fecha_de_nacimiento")
        Genero=serializer.validated_data.get("Genero")
        Numero_de_contacto=serializer.validated_data.get("Numero_de_contacto")
        Email=serializer.validated_data.get("Email")

        serializer.save()


cliente_mixin_view=ClienteMixinView.as_view()

class ClienteUpdateAPIView(generics.UpdateAPIView):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer
    lookup_field="pk"

    def perform_update(self,serializer):
        instance=serializer.save()

cliente_update_view=ClienteUpdateAPIView.as_view()


class ClienteDestroyAPIView(generics.DestroyAPIView):
    queryset=Cliente.objects.all()
    serializer_class=ClienteSerializer
    lookup_field="pk"

    def perform_destroy(self,instance):
        super().perform_destroy(instance)
cliente_destroy_view=ClienteDestroyAPIView.as_view()
