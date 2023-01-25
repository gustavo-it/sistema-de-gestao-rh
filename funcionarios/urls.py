from django.urls import path

from .views import FuncionariosList, FuncionarioEdit

app_name = 'funcionarios'

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update')
]
