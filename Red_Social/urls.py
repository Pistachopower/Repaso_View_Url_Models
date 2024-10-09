from django.urls import path
from . import views

urlpatterns = [
    path('', views.usuario_list, name='usuario_list'),
    path('publicacion', views.publicacion_list, name='publicacion_list'),
    path('comentario', views.comentario_list, name='comentario_list'),
    path('me_gusta', views.me_gusta_list, name='me_gusta_list'),
    path('seguidores', views.seguidores_list, name='seguidores_list'),
]