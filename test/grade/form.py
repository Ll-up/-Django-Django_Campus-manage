from django import forms
from .models import Grade
from django.core.exceptions import ValidationError

class grade_form(forms.ModelForm):

    def clean_grade_name(self):
        grade_name=self.cleaned_data.get('grade_name')
        if len(grade_name)<4 or len(grade_name)>5:
            raise ValidationError("请填写正确的班级")
        return grade_name
    
    def clean_grade_number(self):
        grade_number=self.cleaned_data.get('grade_number')
        if len(grade_number)!=3:
            raise ValidationError('请填写正确的班级编号，三位数字')
        return grade_number

    class Meta:
        model=Grade
        fields=['id','grade_name','grade_number']