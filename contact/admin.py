from django.contrib import admin
from .models import contact
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

class contactModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('message')
admin.site.register(contact , contactModelAdmin)
