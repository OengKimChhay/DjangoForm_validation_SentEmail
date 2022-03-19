from django.urls import path
from . import views

urlpatterns = [
    path('', views.empList, name='listing'),
    path('create/', views.emp, name='create'),
    path('update/<str:pk>/', views.empUpdate, name='update'),
    path('delete/<str:pk>/', views.empDelete, name='delete'),
    path('views/<str:pk>/', views.empView, name='views'),
    path('email/', views.empEmail, name='email'),
    path('social/', views.social, name='social'),
    path('telegram/', views.telegram, name='telegram')
]
