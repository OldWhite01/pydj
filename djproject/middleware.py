class TestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('TestMiddleware - __init__')  # 初始化时执行一次
        
    def __call__(self, request):
        print('TestMiddleware - 请求处理前')  # 在视图处理前执行
        
        response = self.get_response(request)
        
        print('TestMiddleware - 请求处理后')  # 在视图处理后执行
        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('TestMiddleware - process_view')  # 在视图函数调用前执行
        return None
    
    def process_exception(self, request, exception):
        print('TestMiddleware - process_exception')  # 在发生异常时执行
        return None
    
    def process_template_response(self, request, response):
        print('TestMiddleware - process_template_response')  # 在使用模板响应时执行
        return response 