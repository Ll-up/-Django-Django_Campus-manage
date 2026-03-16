from django.contrib import admin
from .models import Teacher

# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display=('id','teacher_name','gender','birthday','contact_number','address')

admin.site.register(Teacher,TeacherAdmin)