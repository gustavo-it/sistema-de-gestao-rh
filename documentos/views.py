from django.views.generic import CreateView

from .models import Documento


class DocumentoCreate(CreateView):
    model = Documento
    fields = ['descricao', 'arquivo']
    
    def form_valid(self, form, *args, **kwargs):
        documento = form.save(commit=False)
        form.instance.pertence_id = self.kwargs['funcionario_id']
        documento.save()
        return super(DocumentoCreate, self).form_valid(form)