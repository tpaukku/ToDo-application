from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ['author', 'text']


admin.site.register(Todo, TodoAdmin)

# Note to self, alternative way of registering to admin
# @admin.register(Todo)
# class TodoAdmin(admin.ModelAdmin):
#     list_display = ['author', 'text']
