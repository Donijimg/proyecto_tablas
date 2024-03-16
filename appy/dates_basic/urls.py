from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name=""),
    path('storage/<str:nombre_admin>/<str:correo_admin>/<str:nombre_user>/<str:correo_user>',views.storage,name="storage"),
    path('consultar/<int:id>',views.consultar,name="consultar"),
    path('modificar/<str:nombre_admin>/<str:nombre_user>/<int:id>',views.modificar,name="modificar"),
    path('eliminar/<int:id>',views.eliminar,name="eliminar"),
    path('consultas',views.consultas,name="consultas")
]