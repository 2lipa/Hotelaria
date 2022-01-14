from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'apphotel'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/', views.admin_edit, name='admin_edit'),
    path('addlocador/', views.create_locador, name='create_locador'),
    path('addlocal/', views.create_local, name='create_local'),
    path('dellocal/<int:id>/', views.delete_local, name='delete_local'),
    path('dellocador/<int:id>/', views.delete_locador, name='delete_locador'),
    path('sellocador/', views.select_locador, name='select_locador'),
    path('rsvlocal/', views.reservar_local, name='reservar_local'),
]
