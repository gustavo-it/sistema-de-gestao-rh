from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import RegistroHoraExtraForm
from .models import RegistroHoraExtra


class HoraExtraList(ListView):
    model = RegistroHoraExtra
    
    def get_queryset(self):
        empresa_logada = self.request.user.funcionario.empresa
        queryset = RegistroHoraExtra.objects.filter(funcionario__empresa=empresa_logada)
        return queryset
    
    
class HoraExtraEdit(UpdateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs
    

class HoraExtraDelete(DeleteView):
    model = RegistroHoraExtra
    success_url = reverse_lazy('registro_hora_extra:list')
    

class HoraExtraCreate(CreateView):
    model = RegistroHoraExtra
    form_class = RegistroHoraExtraForm
    
    def get_form_kwargs(self):
        kwargs = super(HoraExtraCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs