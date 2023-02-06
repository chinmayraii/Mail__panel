from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index),
    path('emp',views.emp),
    path('admins',views.admins),
    path('details',views.details),
    path('add_mail',views.add_mail),
    path('admin_panel',views.admin_panel),
]