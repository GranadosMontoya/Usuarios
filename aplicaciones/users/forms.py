from django import forms
from .models import User

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