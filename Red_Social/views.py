from django.shortcuts import render
from .models import Usuario, Publicacion, Comentario, Me_Gusta, Seguidores

# Create your views here.
def usuario_list(request):
    usuario= Usuario.objects.all()
    return render(request, 'red_social/usuario.html', {'usuario_list':usuario})

def publicacion_list(request):
    publicacion= Publicacion.objects.all()
    return render(request, 'red_social/publicacion.html', {'publicacion_list':publicacion})

def comentario_list(request):
    comentario= Comentario.objects.all()
    return render(request, 'red_social/comentario.html', {'comentario_list': comentario})

def me_gusta_list(request):
    gustas= Me_Gusta.objects.all()
    return render(request, 'red_social/meGusta.html', {'me_gusta_list':gustas})


def seguidores_list(request):
    seguidores= Seguidores.objects.all()
    return render(request, 'red_social/seguidores.html', {'seguidores_list': seguidores})


