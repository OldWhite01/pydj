from django.shortcuts import render
from django.http import FileResponse, HttpResponse, JsonResponse
import os
from django.conf import settings
from pathlib import Path
from django.contrib.auth.models import User
from .models import TestA
from django.views.decorators.csrf import csrf_exempt
import datetime

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

def upload_page(request):
    return render(request, 'helloworld/upload.html')

@csrf_exempt  # 为了简化示例，这里暂时禁用CSRF
def upload_file(request):
    if request.method == 'POST':
        try:
            uploaded_file = request.FILES['file']
            if uploaded_file:
                # 获取桌面路径
                desktop_path = str(Path.home() / "Desktop")
                
                # 生成带时间戳的文件名，避免重名
                timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S_')
                file_name = timestamp + uploaded_file.name
                
                # 构建完整的文件保存路径
                file_path = os.path.join(desktop_path, file_name)
                
                # 保存文件
                with open(file_path, 'wb+') as destination:
                    for chunk in uploaded_file.chunks():
                        destination.write(chunk)
                
                return JsonResponse({
                    'status': 'success',
                    'message': '文件上传成功',
                    'file_name': file_name,
                    'file_path': file_path
                })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'上传失败: {str(e)}'
            }, status=500)
    
    return JsonResponse({
        'status': 'error',
        'message': '请求方法不允许'
    }, status=405)
