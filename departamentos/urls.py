from django.urls import path

from .views import DepartamentoCreate, DepartamentoDelete, DepartamentoList

app_name = 'departamentos'

urlpatterns = [
    path('list/', DepartamentoList.as_view(), name='list'),
    path('novo/', DepartamentoCreate.as_view(), name='create'),
    path('delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete'),
]
