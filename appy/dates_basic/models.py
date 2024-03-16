from django.db import models
from datetime import date


class Admin(models.Model):
  nombre_admin = models.CharField(max_length=200)
  correo_admin = models.CharField(max_length=200)
  fecha_admin = models.DateField(default= date.today)


  def __str__(self):
    return self.nombre_admin
    
class User(models.Model):
  id_User = models.OneToOneField(Admin, on_delete=models.CASCADE, null=True, blank=True)
  nombre_user = models.CharField(max_length=200)
  correo_user = models.CharField(max_length=200)
  fecha_user = models.DateField(default= date.today)
  
  def __str__(self):
    return self.correo_user