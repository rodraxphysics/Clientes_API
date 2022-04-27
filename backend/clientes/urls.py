from django.urls import path
from . import views

urlpatterns=[
    path("",views.cliente_mixin_view),
    path("<int:pk>/",views.cliente_mixin_view),
    path("<int:pk>/update/",views.cliente_update_view),
    path("<int:pk>/delete/",views.cliente_destroy_view)


]
