from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('<int:post>/', views.get_info_about_number_post),
    path('<str:post>/', views.get_name_post),

]

# path('posts/<str:post>', views.get_name_post),
# path('posts/<int:post>', views.get_info_about_number_post),
