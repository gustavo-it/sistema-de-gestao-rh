from django.views.generic import DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .models import Funcionario


class FuncionariosList(ListView):
    model = Funcionario

    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Funcionario.objects.filter(empresa=empresa_logada)
        return queryset
    
class FuncionarioEdit(UpdateView):
    model = Funcionario
    fields = ['nome', 'departamentos',]
    
class FuncionarioDelete(DeleteView):
    model = Funcionario
    success_url = reverse_lazy('funcionarios:list')