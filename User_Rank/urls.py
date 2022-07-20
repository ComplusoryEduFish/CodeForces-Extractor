from django.urls import path
from . import views

app_name = 'User_Rank'
urlpatterns = [
    path('', views.index, name='index'),
    path('rank/', views.rank, name='rank'),
]