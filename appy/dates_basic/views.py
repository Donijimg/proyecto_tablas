from django.shortcuts import render
from django.http import HttpResponse
from .models import Admin,User
# Create your views here.

def index(request):
  users = User.objects.all()
  admins = Admin.objects.all()
  for obj in users:
    print(obj.nombre_user)
  for obj in admins:
    print(obj.nombre_admin)
  return HttpResponse ("lista de nombres")

def storage(request, nombre_admin,correo_admin, nombre_user, correo_user, admin_id):
  users = User(nombre=nombre_user, correo=correo_user, admin_id = admin_id)
  admins = Admin(nombre=nombre_admin, correo=correo_admin)
  users.save()
  admins.save()
  return HttpResponse ("guardamos los datos")
  
def consultar(requets,id):
  user= User.objects.get(id=id)
  admin= Admin.objects.get(id=id)
  print (user)
  print (admin)
  return HttpResponse (f"nombre de usuario: {user.nombre_user}, correo de usuario:{user.correo_user}, fecha del usuario: {user.fecha_user} nombre de admin: {admin.nombre_admin}, correo de admin:{admin.correo_admin}, fecha de admin: {admin.fecha_admin}")



def modificar(request, nombre_user,nombre_admin,id):
  user=User.objects.get(id=id)
  user.nombre_user=nombre_user
  admin=Admin.objects.get(id=id)
  admin.nombre_admin=nombre_admin
  admin.save()
  user.save()
  return HttpResponse("nombre actualizado")

def eliminar(request,id):
  user=User.objects.get(id=id)
  admin=Admin.objects.get(id=id)
  user.delete()
  admin.delete()
  return HttpResponse("id eliminado")

def consultas (request):
  users=User.objects.all()
  admins=Admin.objects.all()
  user=User.objects.get(id= 12)  
  admin=Admin.objects.get(id= 12)

  filtro=User.objects.filter(nombre_user='nombre_user')
  filtro=Admin.objects.filter(nombre_admin='nombre_admin')


#  return HttpResponse("consultas")
  
  limite=User.objects.all()[0:4]
  limite=Admin.objects.all()[0:4]
  order=User.objects.all().order_by('correo_user')[:20]  #-cuerpo
  order=Admin.objects.all().order_by('correo_admin')[:20]  #-cuerpo
  menor=User.objects.filter(id__lte=20)
  menor=Admin.objects.filter(id__lte=20)

  return render(request, "index.html",{
    'users':users,
    'admins':admins,
    'filtro':filtro,
    'user':user,
    'admin':admin,
    'limite':limite,
    'order': order,
    'menor':menor
  })