from django.contrib import admin
from .models import Feedback
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class feedbackModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('description')

admin.site.register(Feedback ,feedbackModelAdmin)
