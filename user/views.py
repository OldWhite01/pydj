from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import TUser
from django.utils import timezone
import hashlib

def index(request):
    return render(request, 'user/index.html')

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
