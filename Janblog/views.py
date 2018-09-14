from django.shortcuts import render, get_object_or_404
from django.utils.safestring import mark_safe
from comments.forms import CommentForm

# Create your views here.
from .models import Article, Category
import markdown
from django.views.generic import ListView

def index(request):
    post_list = Article.objects.all()
    return render(request,'index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Article, pk=pk)

    #浏览数+1
    post.increase_views()
    post.body = mark_safe(markdown.markdown(post.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ]))
    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {
        'post':post,
        'form':form,
        'comment_list':comment_list
    }
    return render(request, 'detail.html', context=context)

def archives(request, year, month):
    post_list= Article.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'index.html', context={'post_list':post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Article.objects.filter(category=cate)
    return render(request, 'index.html', context={'post_list':post_list})