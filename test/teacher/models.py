from django.db import models

# Create your models here.
GENDER_CHOICES=[
    ('M','男'),
    ('F','女'),
]
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=50,verbose_name='姓名')
    gender=models.CharField(max_length=1,choices=GENDER_CHOICES,verbose_name='性别')
    birthday=models.DateField(verbose_name='出生日期',help_text='格式例如：2025-05-01')
    contact_number=models.CharField(max_length=20,verbose_name='联系方式')
    address=models.TextField(verbose_name='家庭住址')

    def __str__(self):
        return self.teacher_name

    class Meta:
        db_table='Teacher'
        verbose_name='教师信息'
        verbose_name_plural='教师信息'