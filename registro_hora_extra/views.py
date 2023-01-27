from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView, UpdateView

from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset
    
    
class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    fields = ['motivo', 'funcionario', 'horas']
    

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('registro_hora_extra:list')