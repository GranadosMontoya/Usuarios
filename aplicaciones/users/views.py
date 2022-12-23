from django.shortcuts import render
from django.views.generic import FormView

from .forms import UserRegistrerForm
from .models import User
# Create your views here.


class UserRegistrerCreateView(FormView):
    template_name = "users/registrer.html"
    form_class = UserRegistrerForm
    success_url = "/"

    def form_valid(self, form):
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero']

        )
        #
        return super(UserRegistrerCreateView, self).form_valid(form)