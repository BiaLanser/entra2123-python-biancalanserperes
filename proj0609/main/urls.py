from django.urls import path
from views import index, hello_world

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('h', hello_world, name = 'hello world'),
]