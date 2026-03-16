import django_filters
from .models import Student, GENDER_CHOICES
from grade.models import Grade

class StudentFilter(django_filters.FilterSet):
    # 学籍号搜索 - 支持部分匹配
    number = django_filters.CharFilter(field_name='number', lookup_expr='icontains', label='学籍号')
    
    # 姓名搜索 - 支持部分匹配
    student_name = django_filters.CharFilter(field_name='student_name', lookup_expr='icontains', label='姓名')
    
    # 性别筛选 - 精确匹配
    gender = django_filters.ChoiceFilter(choices=GENDER_CHOICES, label='性别')
    
    # 班级筛选 - 下拉选择
    grade = django_filters.ModelChoiceFilter(
        queryset=Grade.objects.all().order_by('grade_number'),
        label='班级',
        empty_label='全部班级'
    )
    
    # 联系方式搜索 - 支持部分匹配
    contact_number = django_filters.CharFilter(field_name='contact_number', lookup_expr='icontains', label='联系方式')
    
    # 地址搜索 - 支持部分匹配
    address = django_filters.CharFilter(field_name='address', lookup_expr='icontains', label='家庭住址')
    
    class Meta:
        model = Student
        fields = ['number', 'student_name', 'gender', 'grade', 'contact_number', 'address']

