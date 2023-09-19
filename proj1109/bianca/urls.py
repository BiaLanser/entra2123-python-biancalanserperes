from django.urls import path
from bianca.views import index

app_name = "bianca"

urlpatterns = [
    path('', index, name='index_bianca')

]
