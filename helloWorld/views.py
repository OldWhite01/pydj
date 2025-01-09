from django.shortcuts import render
from django.http import FileResponse, HttpResponse, JsonResponse
import os
from django.conf import settings
from pathlib import Path
from django.contrib.auth.models import User
from .models import TestA

def index(request):
    # 保持原有的 index 视图不变
    if request.method == 'POST':
        content = request.POST.get('content')
        # 保存数据
        test_a = TestA.objects.create(content=content)
        return JsonResponse({'status': 'success', 'content': content})
    print('执行 - index')
    # 获取最新一条数据
    latest_content = TestA.objects.last()
    return render(request, 'index.html', {'content': latest_content.content if latest_content else ''})

def download_page(request):
    # 获取桌面路径
    desktop_path = str(Path.home() / "Desktop")
    file_path = os.path.join(desktop_path, 'a.pptx')
    
    context = {
        'file_name': 'a.pptx',
        'file_path': file_path,
        'file_size': round(os.path.getsize(file_path) / 1024, 2) if os.path.exists(file_path) else 0
    }
    return render(request, 'helloworld/download.html', context)

def download_file(request):
    # 获取桌面路径
    desktop_path = str(Path.home() / "Desktop")
    file_path = os.path.join(desktop_path, 'a.pptx')
    
    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'))
        response['Content-Type'] = 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
        response['Content-Disposition'] = 'attachment; filename="a.pptx"'
        return response
    return HttpResponse("文件不存在", status=404)
