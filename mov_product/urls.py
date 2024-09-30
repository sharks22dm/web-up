from django.urls import path
from . import views

urlpatterns = [
    path('', views.mov_product, name='mov_product')
]
