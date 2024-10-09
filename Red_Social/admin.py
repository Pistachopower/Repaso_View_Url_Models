from django.contrib import admin
from .models import Usuario, Publicacion, Comentario, Me_Gusta, Seguidores
admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Comentario)
admin.site.register(Me_Gusta)
admin.site.register(Seguidores)


