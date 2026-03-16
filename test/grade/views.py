from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin#导入登录判断函数
from .models import Grade
from .form import grade_form
# Create your views here.

class Grade_list(LoginRequiredMixin,ListView):
    model=Grade
    template_name="grade/grade_list.html"
    context_object_name="grade"

class Grade_create(LoginRequiredMixin,CreateView):
    model=Grade
    template_name="grade/form.html"
    form_class=grade_form
    success_url="grade/"
    def form_valid(self, form):
        form.save()
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
    
class Grade_delete(LoginRequiredMixin,DeleteView):
    success_url=reverse_lazy("grade_list")
    model=Grade
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