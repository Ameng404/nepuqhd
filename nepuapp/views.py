from django.shortcuts import render,get_object_or_404
#from django.views.generic import ListView, DetailView
from .models import Column,Article, Post,Category,Paper

def index(request):
    # 取出一篇今日新闻作为新闻摘要
    #paper = Paper.objects.filter(select_reason="校园新闻" or "通知公告")[:0]
    #paper = [i.select_article for i in paper]
    school = Paper.objects.filter(select_reason="校园新闻")[:6]
    school_list = [i.select_post for i in school]
    #notice = Paper.objects.filter(select_reason="通知公告")[6:12]
    #notice_list = [i.select_article for i in notice]
    context={
      #"paper":paper,
      "school_list":school_list,
      #"notice_list":notice_list
    }
    return render(request,'nepu-html/index.html',context=context)

def news(request):
    news_list= Post.objects.all()
    return render(request, 'nepu-html/news.html', context={'news_list':news_list})

def detail(request, pk):
    post_list = Post.objects.all()
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'nepu-html/detail.html', context={'post': post,'post_list': post_list})

"""
class IndexView(ListView):
    model = Post
    template_name = 'nepu-html/index.html'
    home_list = 'post_list'
    paginate_by = 7

"""

"""


def static(request):
    static = Post.objects.all()
    return render(request, 'nepu-html/static.html',context={'static':static})



def category(request, pk):
    # 记得在开始部分导入 Category 类
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'nepu-html/index.html', context={'post_list': post_list})

"""
