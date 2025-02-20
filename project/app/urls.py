
from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('edit/<int:pk>',views.edit,name='edit'),
    path('updatedat/<int:pk>',views.updatedat,name='updatedat'),
    path('login/',views.login,name='login'),
    path('student_list/',views.student_list,name='student_list'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_dashboard/',views.student_dashboard,name='student_dashboard'),
    path('query_list/',views.query_list,name='query_list'),
    path('logout/',views.logout,name='logout'),
    path('delete1/<int:pk1>',views.delete1,name='delete1'),
    path('edit1/<int:pk1>',views.edit1,name='edit1'),
    path('updatedat1/<int:pk1>',views.updatedat1,name='updatedat1'),
    
]