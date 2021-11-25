from django.urls import path
from .views import UsuarioView

urlpatterns = [
    path('Usuarios/', UsuarioView.as_view(), name='Usuarios_list'),
    path('Usuarios/<int:id>', UsuarioView.as_view(), name='Usuarios_process'),
    path('Usuarios/<str:nombre>', UsuarioView.as_view(), name='Usuarios_process_nombre')
]