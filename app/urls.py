from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

from . import views
from .views import ViewPost

urlpatterns = [
    path('', views.home, name='home'),
    path('products/<int:pk>/', ViewPost.as_view(), name='view_posts'),
    path('men/', views.men, name='men'),
    path('women/', views.women, name='women'),
    path('uni/', views.uni, name='uni'),
    path('search/', views.search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)