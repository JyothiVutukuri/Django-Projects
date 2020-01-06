from django.urls import path
from app_two import views

app_name = "Apptwo"

urlpatterns = [

    path('app_two_home/', views.two_home, name="two_home"),
    path('help/', views.help, name="help"),
    path('users/', views.users, name="users"),
    path('form/', views.form_one, name="form"),

]
