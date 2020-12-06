from django.urls import path
from . import views

app_name = 'user_profile'
urlpatterns = [
    path('', views.ProfileListView.as_view(), name='profile-view'),
    path('myprofile/', views.my_profile_view, name='my-profile-view'),
    path('myinvites/', views.invites_received_view, name='my-invites-view'),
    path('all-profiles/', views.ProfileListView.as_view(), name='all-profiles-view'),
    path('to-invite/', views.invite_profiles_list_view, name='invite-profiles-view'),
    path('send-invite/', views.send_invitation, name='send-invite'),
    path('remove-friend/', views.remove_from_friends, name='remove-friend'),
    path('<slug>/', views.ProfileDetailView.as_view(), name='profile-detail-view'),
    path('myinvites/accept/', views.accept_invitation, name='accept-invite'),
    path('myinvites/reject/', views.reject_invitation, name='reject-invite'),
]
