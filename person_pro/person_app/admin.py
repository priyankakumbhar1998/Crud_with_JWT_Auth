from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'address', 'city', 'email', 'gender', 'contact_no', 'aadhar_no' )