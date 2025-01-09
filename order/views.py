from django.shortcuts import render
from django.urls import reverse, resolve
from django.http import HttpResponse

def index(request):
    # 测试 reverse
    url_path = reverse('order:index')  # 获取当前视图的URL
    user_url = reverse('user:index')   # 获取user应用index视图的URL
    main_url = reverse('index')        # 获取主页的URL
    
    # 测试 resolve
    resolver = resolve('/order/')       # 解析URL路径
    
    # 打印结果
    print("\n=== URL 反向解析测试 ===")
    print(f"reverse('order:index') = {url_path}")
    print(f"reverse('user:index') = {user_url}")
    print(f"reverse('index') = {main_url}")
    
    print("\n=== URL 解析测试 ===")
    print(resolver)
    print(f"resolve('/order/').view_name = {resolver.view_name}")
    print(f"resolve('/order/').url_name = {resolver.url_name}")
    print(f"resolve('/order/').app_name = {resolver.app_name}")
    print(f"resolve('/order/').namespace = {resolver.namespace}")
    
    # 在页面上显示结果
    result = f"""
    <h1>Order Index Page</h1>
    <h2>URL 反向解析测试:</h2>
    <p>reverse('order:index') = {url_path}</p>
    <p>reverse('user:index') = {user_url}</p>
    <p>reverse('index') = {main_url}</p>
    
    <h2>URL 解析测试:</h2>
    <p>resolve('/order/').view_name = {resolver.view_name}</p>
    <p>resolve('/order/').url_name = {resolver.url_name}</p>
    <p>resolve('/order/').app_name = {resolver.app_name}</p>
    <p>resolve('/order/').namespace = {resolver.namespace}</p>
    
    <h2>导航链接:</h2>
    <p><a href="{main_url}">返回主页</a></p>
    <p><a href="{user_url}">访问用户页面</a></p>
    """
    
    return HttpResponse(result)
