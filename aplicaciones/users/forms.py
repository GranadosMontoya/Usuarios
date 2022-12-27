from django import forms
from .models import User

from django.contrib.auth import authenticate

class UserRegistrerForm(forms.ModelForm):
    """Form definition for User."""

    password1 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'contraseña'
            }
        )
    )
    password2 = forms.CharField(
        label='Contraseña',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'Repetir contraseña'
            }
        )
    )


    class Meta:
        """Meta definition for Userform."""
        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',
        )
    
    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'las contraseñas no coinciden')
    

class LoginForm(forms.Form):
    username = forms.CharField(
        label='username',
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder':'username',
                'style':'{ margin: 10px }'
            }
        )
    )

    password = forms.CharField(
        label='password',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder':'password',
                'style':'{ margin: 10px }'
            }
        )
    )

    def clean(self):
        clean_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']

        if not authenticate(username=username, password = password):
            raise forms.ValidationError('los datos no son correctos')
        return self.cleaned_data

class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        label='Contraseña actual',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Actual'
            }
        )
    )

    password_new = forms.CharField(
        label='Contraseña nueva',
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder' : 'Contraseña Nueva'
            }
        )
    )

class verificationForm(forms.Form):
    codregistro = forms.CharField(required=True)