from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostCreateForm, PostEditForm


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-date_published']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_details.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post_create.html'


class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    template_name = 'post/post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_delete.html'
    success_url = '/'
