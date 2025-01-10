from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import TestA1
from django.core.paginator import Paginator

class ContentListView(ListView):
    model = TestA1
    template_name = 'order/content_list.html'
    context_object_name = 'contents'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '内容列表'
        return context

class ContentDetailView(DetailView):
    model = TestA1
    template_name = 'order/content_detail.html'
    context_object_name = 'content'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '内容详情'
        return context

class ContentCreateView(CreateView):
    model = TestA1
    template_name = 'order/content_form.html'
    fields = ['chinese', 'english']
    success_url = reverse_lazy('order:content_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '新建内容'
        return context

class ContentUpdateView(UpdateView):
    model = TestA1
    template_name = 'order/content_form.html'
    fields = ['chinese', 'english']
    success_url = reverse_lazy('order:content_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '编辑内容'
        return context

def index(request):
    return render(request, 'order/index.html')
