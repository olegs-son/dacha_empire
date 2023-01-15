from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Post

def index(request):
    template = loader.get_template('posts/index.html')
    context = {
        'posts_list': Post.objects.all()[::-1]
    }
    return HttpResponse(template.render(context, request))

def registration(request):
    pass

def detail_post(request, post_id):
    post = Post.objects.filter(id=1)
    result = "ok"
    return HttpResponse(result)
