from django.urls import path
from membership import views

urlpatterns = [
    path('register/', views.register),
    path('id-maker/', views.id_maker),
    path('contact/', views.contact),
]