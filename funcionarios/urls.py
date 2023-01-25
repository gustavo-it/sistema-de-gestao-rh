from django.urls import path

from .views import FuncionariosList

app_name = 'funcionarios'

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list'),
]
