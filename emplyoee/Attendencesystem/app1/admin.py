from django.contrib import admin
from .models .members import Members
from .models .activity_periods import Activity_periods 
# Register your models here.
admin.site.register(Members)
admin.site.register(Activity_periods)
