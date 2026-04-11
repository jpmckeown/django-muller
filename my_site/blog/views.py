from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from datetime import date

from .models import Post


def get_date(post):
    return post.get('date')


# a View must return an HttpResponse not a string
def index(request):
    latest_posts = Post.objects.all().order_by('date')[:3]
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-2:]
    return render(request, 'blog/index.html', {"posts": latest_posts})


def allposts(request):
    all_posts = Post.objects.all()
    return render(request, 'blog/all-posts.html', {"posts": all_posts})


def onepost(request, slug):
    chosen_post = Post.objects.get(slug=slug)
    # chosen_post = next(x for x in all_posts if x['slug']==slug)
    return render(request, "blog/onepost.html", {
        "post": chosen_post
    })
