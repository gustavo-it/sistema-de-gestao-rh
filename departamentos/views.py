from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Departamento


class DepartamentoList(ListView):
    model = Departamento
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = Departamento.objects.filter(empresa=empresa_logada)
        return queryset

class DepartamentoCreate(CreateView):
    model = Departamento
    fields = ['nome',]
    
    def form_valid(self, form):
        departamento = form.save(commit=False)
        departamento.empresa = self.request.user.funcionario.empresa
        departamento.save()
        return super(DepartamentoCreate,self).form_valid(form)
        