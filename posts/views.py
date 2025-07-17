from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post,  Comentario
from .forms import ComentarioForm
from django.views.generic.edit import FormMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'posts/lista_posts.html'
    context_object_name = 'posts'
    ordering = ['-fecha_publicacion']

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(titulo__icontains=query) | Q(contenido__icontains=query)
            )
        return queryset




class PostDetailView(FormMixin, DetailView):
    model = Post
    template_name = "posts/detalle_post.html"
    context_object_name = 'post'
    form_class = ComentarioForm

    def get_success_url(self):
        return reverse_lazy("detalle_post", kwargs={"pk": self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = self.object.comentarios.all().order_by('-fecha_creacion')
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = self.object
            comentario.autor = self.request.user
            comentario.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'posts/crear_post.html'
    fields = ['titulo', 'contenido', 'imagen']
    success_url = reverse_lazy('lista_posts')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['titulo', 'contenido', 'imagen']
    template_name = 'posts/editar_post.html'

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor

    def get_success_url(self):
        return reverse_lazy('detalle_post', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'posts/eliminar_post.html'
    success_url = reverse_lazy('lista_posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.autor


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, '¡Registro exitoso! Ahora inicia sesión.')
        return response
