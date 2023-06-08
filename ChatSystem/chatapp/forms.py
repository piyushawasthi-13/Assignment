from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Chat
from django.contrib.auth.forms import AuthenticationForm


# Create your forms here.

class NewUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ("Name", "Email", "Gender","DOB","Contact_No","Is_available")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		if commit:
			user.save()
		return user

class EmailAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['Email', 'password']
        
        
class MessageForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea)