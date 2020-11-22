from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('myprofile/', views.my_profile_view, name='my-profile-view')
]