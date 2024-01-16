from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from django.http import HttpResponseForbidden
from . import models


@login_required
def post_list(request):
    posts = models.Post.objects.all()
    return render(request, 'My_posts.html', {'posts': posts})

@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')  # Adjust the URL name as needed
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def edit_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')

    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

@login_required
def delete_post(request, id):
    post = get_object_or_404(models.Post, pk=id)
    post.delete()
    return redirect('home')
