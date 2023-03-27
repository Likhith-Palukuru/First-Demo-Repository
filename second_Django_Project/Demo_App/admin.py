from django.contrib import admin
from Demo_App.models import Student
# Register your models here.

class StudentDisplay(admin.ModelAdmin):
    list_display=['sno','sname','saddr']
    
admin.site.register(Student,StudentDisplay)
