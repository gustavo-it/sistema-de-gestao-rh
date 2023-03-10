from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from departamentos.models import Departamento
from empresas.models import Empresa


class Funcionario(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome do funcionário")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True, blank=True)
    
    def get_absolute_url(self):
        return reverse('funcionarios:list')
    
    def __str__(self):
        return self.nome