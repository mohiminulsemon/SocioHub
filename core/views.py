from django.shortcuts import render
from Posts.models import Post, Comment
from Posts import forms
# Create your views here.



def home(request):
    posts = Post.objects.all()
    comments = Comment.objects.all()  # Fetch all comments
    comment_form = forms.CommentForm()
    return render(request, 'index.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})