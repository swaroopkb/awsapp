from django.urls import path
from p1app import views


urlpatterns = [
    path('', views.users,name='users'),

]
