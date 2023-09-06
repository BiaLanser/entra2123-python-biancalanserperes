from django.urls import path
from main.views import index, hello_world, bia

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('h', hello_world, name = 'hello world'),
    path('b', bia, name = 'bia'),
]

    
