from django.urls import include, path

from .views import home

app_name = 'funcionarios'

urlpatterns = [
    path('', home),
]
