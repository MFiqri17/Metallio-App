from os import name
from django.urls import path
from . import views 

urlpatterns = [
    path('dashboard/', views.dashboard, name="dashboard"),
    path('register/', views.Register, name="register"),
    path('login/', views.Login, name='login'),
    path('beranda/<pk>/', views.Beranda, name='beranda'),
    path('event/<pk>/', views.Events, name='Event'),
    path('daftarMetallio/<pk>/', views.MetallioRegis, name="Daftar"),
    path('daftarPilihan/<pk>/', views.MetallioPilihan, name="DaftarPilihan")
]

