from django.urls import path
from bianca.views import index, ex001, ex003

app_name = "bianca"

urlpatterns = [
    path('', index, name='index_bianca'),
    path('ex001', ex001, name='ex001'),
    path('ex003', ex003, name='ex003'),
]
