
from unicodedata import name
from django.urls import path
from news_app import views

urlpatterns = [
   
    path('', views.home),
    path('home/', views.home, name='home'),
    path ('add', views.add, name='add' ),
    path('edit/<int:id>', views.edit, name='edit'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('login/', views.signin, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.signout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset/', views.reset, name='reset'),
]