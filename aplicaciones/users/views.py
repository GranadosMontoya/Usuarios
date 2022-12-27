from django.shortcuts import render
from django.views.generic import FormView , View, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from .funcionts import code_generator
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .forms import UserRegistrerForm, LoginForm, UpdatePasswordForm, verificationForm
from .models import User
# Create your views here.


class UserRegistrerCreateView(FormView):
    template_name = "users/registrer.html"
    form_class = UserRegistrerForm
    success_url = "/"

    def form_valid(self, form):
        #
        #genero el codigo
        codigo = code_generator()
        #
        User.objects.create_user(
            form.cleaned_data['username'],
            form.cleaned_data['email'],
            form.cleaned_data['password1'],
            nombres = form.cleaned_data['nombres'],
            apellidos = form.cleaned_data['apellidos'],
            genero = form.cleaned_data['genero'],
            codregistro = codigo
        )
        #enviar el codigo al usuario
        asunto = 'confirmación de email'
        mensaje = 'Su codigo de verificación es: '+codigo
        email_remitente = 'sebasmontoya2107@hotmail.com'
        #send mail
        send_mail(asunto, mensaje, email_remitente, [form.cleaned_data['email']],)
        #redirigir a pantalla de validacion
        return HttpResponseRedirect(
            reverse(
                'user_app:verification'
            )
        )


class Login(FormView):
    template_name = 'users/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_app:panel')

    def form_valid(self, form):
        user = authenticate(
            username = form.cleaned_data['username'],
            password = form.cleaned_data['password']
        )
        login(self.request, user)
        return super().form_valid(form)

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(
            reverse(
                'user_app:login'
            )
        )


class UpdatePasswordView(LoginRequiredMixin, FormView):
    template_name = "users/update.html"
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('user_app:login')
    login_url = ('user_app:login')

    def form_valid(self, form):
        usuario = self.request.user
        user = authenticate(
            username = usuario.username,
            password = form.cleaned_data['password']
        )
        if user:
            new_password = form.cleaned_data['password_new']
            usuario.set_password(new_password)
            usuario.save()
        Logout()
        return super().form_valid(form)

class CodeVerificationView(FormView):
    template_name = 'users/verification.html'
    form_class = verificationForm
    success_url = reverse_lazy('user_app:login')

    def form_valid(self, form):
        #
        return super().form_valid(form)