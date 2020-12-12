from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Post
from blog.forms import PostCreateForm, PostEditForm
from django.http import HttpResponseRedirect


class IndexView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-date_published']


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        current_post = get_object_or_404(Post, id=self.kwargs['pk'])

        has_liked = False
        if current_post.likes.filter(id=self.request.user.id).exists():
            has_liked = True
        context['has_liked'] = has_liked

        total_likes = current_post.likes_count()
        context['total_likes'] = total_likes

        return context


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
    success_url = reverse_lazy('index')


def post_like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('full post', args=[str(pk)]))
