from django import forms


from .models import Household, User, Wallet

class UserForm(forms.ModelForm):
	class Meta:
		model = User