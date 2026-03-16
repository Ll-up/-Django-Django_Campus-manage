from django.contrib import admin
from grade.models import Grade
# Register your models here.
class GradeAdmin(admin.ModelAdmin):
   #配置展示列表
    list_display=('id','grade_number','grade_name')
   #配置过滤字段
    list_filter=('id','grade_number','grade_name')
admin.site.register(Grade,GradeAdmin)
