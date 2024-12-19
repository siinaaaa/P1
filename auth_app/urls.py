from django.urls import path
from . import views

app_name = 'auth_app'
urlpatterns = [
    path('login', views.image_processing, name='image_processing'),
    path('logout', views.log_out, name='logout'),
    path('register', views.Register, name='register'),
]
