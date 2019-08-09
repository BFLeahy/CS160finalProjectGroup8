from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('editor/', views.editor, name="editor"),
    path('home/', views.home, name="home"),
]