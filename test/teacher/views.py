from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from .models import Teacher
from rest_framework.views import APIView
from .serializers import TeacherlistSerializers
from rest_framework import status
from .form import Teacher_Form
from django.contrib.auth.mixins import LoginRequiredMixin#导入登录判断函数
# Create your views here.

class Teacher_list(LoginRequiredMixin,ListView):
    model=Teacher
    template_name="teacher/teacher_list.html"
    context_object_name="teacher"

class Teacher_create(LoginRequiredMixin,CreateView):
    model=Teacher
    template_name="teacher/teacher_form.html"
    form_class=Teacher_Form
    success_url='teacher/teacher_list'

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
    
class Teacher_update(LoginRequiredMixin,UpdateView):
    model=Teacher
    template_name="teacher/teacher_form.html"
    form_class=Teacher_Form
    success_url=reverse_lazy("teacher_list")


class Teacher_delete(LoginRequiredMixin,DeleteView):
    success_url=reverse_lazy("teacher_list")
    model=Teacher
    def delete(self, request, *args, **kwargs):
        self.object=self.get_object()
        try:
            self.object.delete()
            return JsonResponse({
                'status':'success',
                'messages':'删除成功'
            },stauts=200)
        except Exception as e:
            return JsonResponse({
                'status':'error',
                'messages':'删除失败'
            },stauts=500)
        

        
def tailwind(request):
    return render(request,'tailwind-try.html')

#API化实现后端发送JS数据
class TeacherList(APIView):
    #展示教师
    def get(self,request):
        query=Teacher.objects.all()
        serializers=TeacherlistSerializers(query,many=True)
        return JsonResponse(serializers.data,safe=False,status=status.HTTP_200_OK)
    #新增教师
    def post(self,request):
        ser=TeacherlistSerializers(data=request.data)
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=status.HTTP_201_CREATED)
        return JsonResponse(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    #删除教师
    def delete(self,request,pk):
        try:
            teacher = Teacher.objects.get(pk=pk)

        except Teacher.DoesNotExist:
            return JsonResponse({'detail': '未找到'}, status=status.HTTP_404_NOT_FOUND)
        teacher.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)