from django.contrib import admin
from .models import Students,CollegeCode, Faculty

# Register your models here.

admin.site.register(CollegeCode)
admin.site.register(Faculty)
admin.site.register(Students)