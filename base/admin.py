# base/admin.py

from django.contrib import admin
from .models import Task

# Register the Task model with the admin site
# This allows the admin site to have access to the Task model
admin.site.register(Task)
