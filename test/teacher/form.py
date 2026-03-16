from django import forms
import datetime
from .models import Teacher
from grade.models import Grade 
from django.core.exceptions import ValidationError

class Teacher_Form(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=['id','teacher_name','gender','birthday','contact_number','address']

    def clean_teacher_name(self):
        teacher_name = self.cleaned_data.get('teacher_name')
        if len(teacher_name) < 2 or len(teacher_name) > 50:
            raise ValidationError('请填写正确的教师姓名')
        return teacher_name
    
    def clean_birthday(self):
        birthday = self.cleaned_data.get('birthday')
        if not isinstance(birthday, datetime.date):
            raise ValidationError('生日格式错误，正确格式例如：2020-05-01')
        if birthday > datetime.date.today():
            raise ValidationError('生日应该在今天之前。')
        return birthday
    
    def clean_contact_number(self):
        contact_number = self.cleaned_data.get('contact_number')
        if len(contact_number) != 11:
            raise ValidationError('联系电话应为11位。')
        return contact_number