from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView


class Homeview(TemplateView):
    template_name = 'base.html'
