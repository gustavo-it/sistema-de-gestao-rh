from django.urls import path

from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete, FuncionarioCreate

app_name = 'funcionarios'

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list'),
    path('novo/', FuncionarioCreate.as_view(), name='create'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete'),
]
