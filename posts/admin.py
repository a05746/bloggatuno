from django.contrib import admin
from .models import Post
from .models import Comentario


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'autor', 'fecha_publicacion')
    search_fields = ('titulo', 'contenido', 'autor__username')
    list_filter = ('fecha_publicacion', 'autor')
    list_per_page = 10


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'autor', 'fecha_creacion')
    search_fields = ('post_titulo', 'autor_username', 'contenido')
    list_filter = ('fecha_creacion',)
    list_per_page = 10
    

 


