from django import forms
import datetime
from .models import Student 
from grade.models import Grade
from django.core.exceptions import ValidationError

class Student_Form(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.get('grade').queryset = Grade.objects.all().order_by('grade_number')

    def clean_student_name(self):#这里重写了对应字段的检验方法
        student_name = self.cleaned_data.get('student_name')
        if len(student_name) < 2 or len(student_name) > 50:
            raise ValidationError('请填写正确的学生姓名')
        return student_name
    

    def clean_student_number(self):
        student_number = self.cleaned_data.get('student_number')
        if len(student_number) != 19:
            raise ValidationError('学号长度应为19位。')
        return student_number
    
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if not isinstance(birthday, datetime.date):
            raise ValidationError('生日格式错误，正确格式例如：2020-05-01')
        if birthday > datetime.date.today():
            raise ValidationError('生日应该在今天之后。')
        return birthday
    
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if len(contact_number) != 11:
            raise ValidationError('联系电话应为11位。')
        return contact_number

    class Meta:
        model=Student
        fields=['id','number','student_name','gender','birthday','contact_number','address','grade']
