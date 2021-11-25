from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from .models import Usuario
import json

# Create your views here.

class UsuarioView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request , nombre):
        if (len(nombre) > 0):
            usuarios = list(Usuario.objects.filter(nombre=nombre).values())
            if len(usuarios) > 0:
                usuario = usuarios[0]
                datos = {'message': "Success", 'Usuario': usuario}
            else:
                datos = {'message': "Usuario no encontrado..."}
            return JsonResponse(datos)
        else:
            usuarios = list(Usuario.objects.values())
            if len(usuarios) > 0:
                datos = {'message': "Success", 'Usuarios': usuarios}
            else:
                datos = {'message': "Usuario no encontrado..."}
            return JsonResponse(datos)

    def post(self, request):
        jd = json.loads(request.body)
        Usuario.objects.create(correo=jd['correo'], nombre=jd['nombre'], password=jd['password'])
        datos = {'message': "Success"}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            usuario = Usuario.objects.get(id=id)
            usuario.correo = jd['correo']
            usuario.nombre = jd['nombre']
            usuario.password = jd['password']
            usuario.save()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)

    def delete(self, request, id):
        usuarios = list(Usuario.objects.filter(id=id).values())
        if len(usuarios) > 0:
            Usuario.objects.filter(id=id).delete()
            datos = {'message': "Success"}
        else:
            datos = {'message': "Usuario no encontrado..."}
        return JsonResponse(datos)


   
  
