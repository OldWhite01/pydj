from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TUser
from django.utils import timezone
import hashlib

def index(request):
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        
        # 检查用户名是否已存在
        if TUser.objects.filter(user_name=username).exists():
            return JsonResponse({'status': 'error', 'message': '用户名已存在'}, status=400)
            
        # 检查邮箱是否已存在
        if TUser.objects.filter(user_email=email).exists():
            return JsonResponse({'status': 'error', 'message': '邮箱已被注册'}, status=400)
        
        # 创建新用户
        try:
            user = TUser.objects.create(
                user_name=username,
                user_pass=password,
                user_email=email,
                create_time=timezone.now()
            )
            return JsonResponse({'status': 'success', 'message': '注册成功'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return render(request, 'user/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # 对密码进行MD5加密
        md5 = hashlib.md5()
        md5.update(password.encode())
        encrypted_password = md5.hexdigest()
        
        
        try:
            user = TUser.objects.get(user_name=username, user_pass=password)
            # 更新最后登录时间
            user.modify_time = timezone.now()
            user.save()
            
            # 将用户信息存入session
            request.session['user_id'] = user.id
            request.session['username'] = user.user_name
            
            return JsonResponse({'status': 'success', 'message': '登录成功'})
        except TUser.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': '用户名或密码错误'}, status=400)
    
    return render(request, 'user/login.html')

def logout(request):
    # 清除session
    request.session.flush()
    return redirect('user:login')
