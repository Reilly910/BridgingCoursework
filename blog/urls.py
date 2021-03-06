from django.urls import path
from . import views;

urlpatterns = [

    path('posts', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('', views.main_page, name="main_page"),
    path('CV', views.CV, name='CV'),
]