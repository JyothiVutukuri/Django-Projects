from django.contrib import admin
from app_two.models import MyUser, Profile

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Profile)
