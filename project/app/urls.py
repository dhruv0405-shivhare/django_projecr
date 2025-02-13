
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('updatedat/<int:pk>',views.updatedat,name='updatedat'),
    path('login/',views.login,name='login'),
    
]