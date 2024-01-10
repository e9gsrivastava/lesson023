from django.contrib import admin
from .models import Student
from .models import Teacher

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] 

admin.site.register(Student, StudentAdmin)


class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'email'] 

admin.site.register(Teacher, TeacherAdmin)