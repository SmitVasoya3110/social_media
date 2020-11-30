from django.urls import path
from .views import post_comment_create_list_view, like_unlike_post

app_name = 'post'

urlpatterns = [
    path('', post_comment_create_list_view, name='main-post-view'),
    path('liked', like_unlike_post, name='liked-post-view'),

]