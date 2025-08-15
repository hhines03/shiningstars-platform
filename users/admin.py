from django.contrib import admin
from .models import CustomUser , Child

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Child)