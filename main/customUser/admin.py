from django.contrib import admin
from .models import User, TestModel


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(TestModel)
class TestModelAdmin(admin.ModelAdmin):
    pass

