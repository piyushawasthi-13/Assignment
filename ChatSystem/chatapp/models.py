from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import MinLengthValidator
from django.core.exceptions import ValidationError
from datetime import date
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
# model of user User
Gender_choice=(
    ("Male","Male"),
    ("Female","Female"),
    ("others","others")
)
phone_regex = RegexValidator(
    regex=r'^\d{10}$',
    message='Phone number must be 10 digits'
)
def validate_past_date(value):
    if value > date.today():
        raise ValidationError("Date of birth cannot be in the future.")
    
class User(AbstractBaseUser, PermissionsMixin):
    Name=models.CharField(max_length=60)
    Email = models.EmailField(unique=True)
    Gender=models.CharField(max_length=100,choices=Gender_choice,null=True,blank=True)
    DOB=models.DateField(validators=[validate_past_date],null=True,blank=True)
    Contact_No=models.CharField(max_length=10,validators=[phone_regex],null=True,blank=True)
    Is_available=models.BooleanField(default=False)
    Created_at=models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'Email'
    REQUIRED_FIELDS = ['Name']

    def __str__(self):
        return self.Email


#models of chat

class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_chats')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_chats')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} -> {self.receiver}: {self.message}"