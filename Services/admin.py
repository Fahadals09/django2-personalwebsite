from django.contrib import admin
from .models import Services
from django_summernote.admin import SummernoteModelAdmin



# Register your models here.

class ServicesModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description')
admin.site.register(Services , ServicesModelAdmin)
