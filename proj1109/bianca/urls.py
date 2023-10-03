from django.urls import path
from bianca.views import *

app_name = "bianca"

urlpatterns = [
    path('', index, name='index_bianca'),
    path('ex001', ex001, name='ex001'),
    path('ex003', ex003, name='ex003'),
    path('ex004', ex004, name='ex004'),
    path('ex005', ex005, name='ex005'),
]