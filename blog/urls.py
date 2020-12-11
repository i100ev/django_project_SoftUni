from django.urls import path

from blog.views import IndexView, PostDetailView, PostCreateView, PostEditView, PostDeleteView, post_like

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('post/<int:pk>', PostDetailView.as_view(), name='full post'),
    path('post/create/', PostCreateView.as_view(), name='create post'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='edit post'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='delete post'),
    path('post/like/<int:pk>', post_like, name='like post'),
]
