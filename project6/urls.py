from django.contrib import admin
from django.urls import path

from signup import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('doLogin/', views.doLogin),
    path('home/', views.doLogin),
    path('blank/', views.blank),
    path('register/', views.register),
    path('error/', views.error),
    path('forgot_password/', views.forgot_password)
]
