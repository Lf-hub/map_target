from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Target


class TargetIndex(ListView):
    model = Target
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['map_data'] = self.get_map_data()
        return context

    def get_map_data(self):
        # Obtém dados para o mapa, neste exemplo, as coordenadas dos alvos
        targets = Target.objects.all()
        map_data = []

        for target in targets:
            map_data.append({
                'nome': target.name,
                'latitude': target.latitude,
                'longitude': target.longitude,
            })

        return map_data