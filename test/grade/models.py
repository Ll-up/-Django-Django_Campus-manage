from django.db import models
from teacher.models import Teacher

# Create your models here.
class Grade(models.Model):
    grade_name=models.CharField(max_length=50,unique=True,verbose_name='班级名称')
    grade_number=models.CharField(max_length=10,unique=True,verbose_name='班级编号')
    teachers=models.ManyToManyField(Teacher)

    def __str__(self):
        return self.grade_name
    
    class Meta:
        db_table='grade'#数据表名字
        verbose_name='班级'#定义模型的对象名称
        verbose_name_plural='班级名称'#表示模型的复数名字，既它在django管理界面其显示的名称
