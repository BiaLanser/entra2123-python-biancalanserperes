from django.contrib import admin
from django.urls import path, include
from angeline.views import index, ex002, contato

app_name = "angeline"

urlpatterns = [
    path('helloworld', index, name='index'),
    path('', ex002, name='ex002'),
    path('contato', contato, name='contato'),

]
