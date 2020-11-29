from django.urls import path
from .views import post_comment_create_list_view

app_name = 'post'

urlpatterns = [
    path('', post_comment_create_list_view, name='main-post-view')
]