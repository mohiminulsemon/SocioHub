from django.shortcuts import render
from Posts.models import Post, Comment
from Posts import forms
from .constants import USER_SPOTLIGHT_DATA, LATEST_NEWS_DATA
# Create your views here.



def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()
    comment_form = forms.CommentForm()

    # Fetch data for UserSpotlight and Latest News from constants.py
    user_spotlight_data = USER_SPOTLIGHT_DATA
    latest_news_data = LATEST_NEWS_DATA

    context = {
        'posts': posts,
        'comments': comments,
        'comment_form': comment_form,
        'user_spotlight_data': user_spotlight_data,
        'latest_news_data': latest_news_data,
    }

    return render(request, 'index.html', context)