from django.urls import path
from .views import index, bfhl_post, bfhl_get

urlpatterns = [
    path('', index, name='index'),
    path('bfhl', bfhl_post, name='bfhl_post'),
    path('bfhl', bfhl_get, name='bfhl_get'),
]
