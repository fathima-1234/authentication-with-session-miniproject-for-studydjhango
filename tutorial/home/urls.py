from django.urls import path,include
from . import views

urlpatterns = [
     path('', views.login_user, name="login_user"),   
     path('logout_user/', views.logout_user, name='logout_user'),
     path('home/', views.index, name = 'home' ),
     path('about/',views.about, name = 'about'),
     path('places/',views.places,name = 'places'),
     path('register/',views.register,name = 'register'),
]