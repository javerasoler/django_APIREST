from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser): 
    pass
    email = models.EmailField(unique=True) #Aparece una vez en la base de datos
    
    linkedin = models.CharField(max_length=255, blank=True)
    
    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = []