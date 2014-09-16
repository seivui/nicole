from django.contrib import admin

# Register your models here.
from .models import Household, User, Wallet

class HouseholdAdmin(admin.ModelAdmin):
	class Meta:
		model =  Household

class UserAdmin(admin.ModelAdmin):
	class Meta:
		model = User

class WalletAdmin(admin.ModelAdmin):
	class Meta:
		model = Wallet

admin.site.register(Household, HouseholdAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Wallet, WalletAdmin)