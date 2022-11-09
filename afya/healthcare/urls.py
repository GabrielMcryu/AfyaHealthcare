from django.urls import path
from . import views

app_name = 'healthcare'

urlpatterns = [
    path('register/', views.registerView, name='register'),
    path('finish/', views.finishView, name='finish'),
    path('dashboard/', views.dashBoardView, name='dashboard'),
]