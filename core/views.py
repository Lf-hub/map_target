from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from core.forms import TargetForm

from core.models import Target


class TargetIndex(ListView):
    model = Target
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_data'] = self.get_map_data()
        return context

    def get_map_data(self):
        # Obtém as coordenadas dos alvos
        targets = Target.objects.all()
        map_data = []

        for target in targets:
            map_data.append({
                'nome': target.name,
                'latitude': target.latitude,
                'longitude': target.longitude,
            })

        return map_data

class TargetList(ListView):
    model = Target
    template_name = 'target_list.html'

class TargetCreate(CreateView):
    model = Target
    template_name = 'target_create.html'
    success_url = reverse_lazy('core:list')
    form_class = TargetForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(TargetCreate, self).get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TargetUpdate(UpdateView):
    model = Target
    template_name = 'target_detail.html'
    fields = ['name', 'latitude', 'longitude']
    success_url = reverse_lazy('core:list')

class TargetDelete(DeleteView):
    model = Target
    template_name = 'target_delete.html'
    
    def get_success_url(self):
        return reverse_lazy("core:list")