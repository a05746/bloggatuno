from . import views
from django.urls import path
from .views import RegisterView
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)

urlpatterns = [
    path('', PostListView.as_view(), name='lista_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='detalle_post'),
    path('post/nuevo/', PostCreateView.as_view(), name='crear_post'),
    path('post/<int:pk>/editar/', PostUpdateView.as_view(), name='editar_post'),
    path('post/<int:pk>/eliminar/', PostDeleteView.as_view(), name='eliminar_post'),
    path('register/', RegisterView.as_view(), name='register'),
]


