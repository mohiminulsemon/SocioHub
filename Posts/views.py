from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm,CommentForm
from django.http import HttpResponseForbidden
from . import models
from . import forms
from django.contrib import messages


@login_required
def my_posts(request):
    comments = models.Comment.objects.all()  # Fetch all comments
    user_posts = models.Post.objects.filter(author=request.user)
    return render(request, 'My_posts.html', {'posts': user_posts, 'comments': comments})


@login_required
def post_details(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)

    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Comment added successfully!')

    comments = models.Comment.objects.filter(post=post)
    comment_form = forms.CommentForm()

    return render(request, 'post_details.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


@login_required
def post_list(request):
    if request.method == 'POST':
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            
            # Extract user_id and post_id from the form data
            user_id = request.user.id
            post_id = request.POST.get('post_id')

            # Set user_id and post_id for the comment
            new_comment.user_id = user_id
            new_comment.post_id = post_id
            new_comment.save()

            messages.success(request, 'Comment added successfully!')
    
    posts = models.Post.objects.all()
    comments = models.Comment.objects.all()  # Fetch all comments
    comment_form = forms.CommentForm()

    return render(request, 'All_posts.html', {'posts': posts, 'comments': comments, 'comment_form': comment_form})


@login_required
def like_post(request, post_id):
    post = get_object_or_404(models.Post, id=post_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'like':
            post.likes.add(request.user)
        elif action == 'unlike':
            post.likes.remove(request.user)

    return redirect('home')


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
def delete_post(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.delete()
    return redirect('home')


# comment section
@login_required
def toggle_edit_comment(request, comment_id):
    comment = get_object_or_404(models.Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You don't have permission to edit this comment.")

    comment.edit_mode = not comment.edit_mode
    comment.save()

    return redirect('home')


@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(models.Comment, id=comment_id)

    if comment.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this comment.")

    comment.delete()
    return redirect('home')