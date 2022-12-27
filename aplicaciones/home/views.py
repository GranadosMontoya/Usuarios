from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
import datetime
from django.views.generic import TemplateView
# Create your views here.





# class fechaMixixn(object):

#     def get_context_data(self, **kwargs):
#         context = super(fechaMixixn, self).get_context_data(**kwargs)
#         context['fecha'] = datetime.datetime.now()
#         return context


class TemplatePrueba(TemplateView):
    template_name = "home/mixing.html"

class HomePage(LoginRequiredMixin,TemplateView):
    template_name = "home/index.html"
    login_url = reverse_lazy('user_app:login')