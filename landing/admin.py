from django.contrib import admin
from .models import *

class SubscriberAdmin(admin.ModelAdmin):
    #list_display = ['name', 'email']
    list_display =  [field.name for field in Subscribers._meta.fields]
    #fields = ['name']
    #exclude = ['email']
    list_filter = ['name',]
    search_fields = ['name']
    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscriberAdmin)