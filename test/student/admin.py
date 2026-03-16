from django.contrib import admin
from student.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
   #配置展示列表
    list_display=('id','number','student_name','gender','birthday','contact_number','address')
   #配置过滤字段
    list_filter=('id','number','student_name','gender','birthday','contact_number','address')
admin.site.register(Student,StudentAdmin)
