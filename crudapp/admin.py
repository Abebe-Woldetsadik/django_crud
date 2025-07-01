from django.contrib import admin
from .models import UserModel, Gender
# Register your models here.

admin.site.register(UserModel)
admin.site.register(Gender)
