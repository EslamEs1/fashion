from django.urls import path
from .views import PostListView, PostDetailView, comment


app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/', comment, name='add_comment'),
]
