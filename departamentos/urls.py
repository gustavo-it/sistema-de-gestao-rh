from django.urls import path

from .views import DepartamentoList

app_name = 'departamentos'

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list'),
]
