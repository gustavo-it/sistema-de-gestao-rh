from django.urls import path

from .views import FuncionariosList, FuncionarioEdit, FuncionarioDelete

app_name = 'funcionarios'

urlpatterns = [
    path('', FuncionariosList.as_view(), name='list'),
    path('editar/<int:pk>/', FuncionarioEdit.as_view(), name='update'),
    path('delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete'),
]
