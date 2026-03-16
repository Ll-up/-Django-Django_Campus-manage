from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Student
from .forms import Student_Form
from .filters import StudentFilter
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin#导入登录判断函数

# Create your views here.
class Student_list(LoginRequiredMixin,ListView):
    model=Student
    template_name="student/student_list.html"
    context_object_name='student'#指定模板中使用的上下文变量名
    
    def get_queryset(self):
        queryset = Student.objects.all().select_related('grade')#把 Student 整张表的所有记录取出来，顺便一次性把每条记录关联的 grade 外键对象也一起从数据库拉回来
        self.filterset = StudentFilter(self.request.GET, queryset=queryset)#queryset=queryset 就是给过滤器划定筛选范围，让它不再重复查库，同时保留你之前所有的预处理和优化。
        return self.filterset.qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 确保filterset已初始化
        if not hasattr(self, 'filterset'):
            queryset = Student.objects.all().select_related('grade')
            self.filterset = StudentFilter(self.request.GET, queryset=queryset)
        context['filter'] = self.filterset
        return context

class Student_create(LoginRequiredMixin,CreateView):
    model=Student
    template_name="student/forms.html"
    form_class=Student_Form
    success_url="student/"
    def form_valid(self, form):
        form.save()

        # 返回json响应
        return JsonResponse({
            'status': 'success',
            'messages': '操作成功'
        }, status=200)
    
    def form_invalid(self, form):
        errors = form.errors.as_json()
        return JsonResponse({
            'status': 'error',
            'messages': errors
        }, status=400)
    
class Student_update(LoginRequiredMixin,UpdateView):
    model=Student
    template_name="student/forms.html"
    form_class=Student_Form
    success_url=reverse_lazy("student_list")


class Student_delete(LoginRequiredMixin,DeleteView):
    success_url=reverse_lazy("student_list")
    model=Student
    def delete(self, request, *args, **kwargs):
        self.object=self.get_object()
        try:
            self.object.delete()
            return JsonResponse({
                'status':'success',
                'messages':'删除成功'
            },status=200)
        except Exception as e:
            return JsonResponse({
                'status':'error',
                'messages':'删除失败'
            },status=500)
