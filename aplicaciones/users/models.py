from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    """Model definition for User."""
   
    GENDER_CHOCICES = (
        ('M','Maculino'),
        ('F','Femenino'),
        ('O','Otros')
    )
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField()
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    genero = models.CharField(max_length=1, choices=GENDER_CHOCICES, blank=True)
    USERNAME_FIELD = 'username'
    
    def get_short_name(self):
        return self.username
    def get_full_name(self):
        return self.nombres + ' '+self.apellidos



    class Meta:
        """Meta definition for User."""
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        """Unicode representation of User."""
        pass
