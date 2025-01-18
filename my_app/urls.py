from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload_photo/', views.upload_photo, name='upload_photo'),
    path('profile/', views.profile, name='profile'),
    path('like_photo/<int:photo_id>/', views.like_photo, name='like_photo'),
    path('unlike_photo/<int:photo_id>/', views.unlike_photo, name='unlike_photo'),
    path('delete_photo/<int:photo_id>/', views.delete_photo, name='delete_photo'),
]
