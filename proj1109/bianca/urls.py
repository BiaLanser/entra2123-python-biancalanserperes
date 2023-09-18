from django.urls import path
from bianca.views import index
urlpatterns = [
    path('', index, name='index_bianca')

]
