from my_app import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('upload/', views.upload_photo, name='upload_photo'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('login/', views.login_view, name='login'),
    path('like/<int:photo_id>/', views.like_photo, name='like_photo'),  
    path('unlike/<int:photo_id>/', views.unlike_photo, name='unlike_photo'),  
    path('delete/<int:photo_id>/', views.delete_photo, name='delete_photo'),  
]
