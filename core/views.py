from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.models import Target


class TargetIndex(ListView):
    model = Target
    template_name = 'index.html'