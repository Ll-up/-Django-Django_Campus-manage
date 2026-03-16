from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .forms import LoginForm, RegisterForm
import json

# Create your views here.
def login_view(request):
    """登录视图"""
    if request.user.is_authenticated:
        return redirect('/')  # 已登录用户重定向到首页
    
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)#此处将表单得到的账号密码与数据库中信息进行比对
            
            if user is not None:
                login(request, user)
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':#用于判断是否是异步请求
                    return JsonResponse({
                        'status': 'success',
                        'message': '登录成功',
                        'redirect_url': '/'
                    })
                return redirect('/')
            else:
                error_msg = '用户名或密码错误'
        else:
            error_msg = '请检查输入信息'
        
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'status': 'error',
                'message': error_msg
            })
        messages.error(request, error_msg)
    else:
        form = LoginForm()
    
    return render(request, "login.html", {'form': form})

def register_view(request):
    """注册视图"""
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'status': 'success',
                        'message': '注册成功',
                        'redirect_url': '/'
                    })
                return redirect('/')
        else:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {}
                for field, error_list in form.errors.items():
                    errors[field] = [{'message': error} for error in error_list]
                return JsonResponse({
                    'status': 'error',
                    'message': '注册失败',
                    'errors': errors
                })
            messages.error(request, '注册失败，请检查输入信息')
    else:
        form = RegisterForm()
    
    return render(request, "login.html", {'register_form': form})

@login_required
def logout_view(request):
    """登出视图"""
    logout(request)
    return redirect('/login/')

def main_l(request):
    """主登录页面"""
    return login_view(request)