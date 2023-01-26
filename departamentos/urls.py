from django.urls import path

from .views import DepartamentoList, DepartamentoCreate

app_name = 'departamentos'

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list'),
    path('novo/', DepartamentoCreate.as_view(), name='create'),
]
