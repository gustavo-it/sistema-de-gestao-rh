from django.urls import path

from .views import EmpresaCreate

app_name = 'empresas'

urlpatterns = [
    path('novo/', EmpresaCreate.as_view(), name='create_empresa')
]
