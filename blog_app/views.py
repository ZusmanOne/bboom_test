from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, User
from django.db import transaction

from .forms import PostForm


def get_users(request):
    users = User.objects.all()
    return render(request, 'users.html', context={'users': users})


def get_user_posts(request, pk):
    user = get_object_or_404(User, pk=pk)
    user_posts = Post.objects.select_related('user').filter(user=user)
    return render(request, 'user_posts.html', context={'posts': user_posts})


@transaction.atomic
def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {'post': post}
    if request.method == 'GET':
        return render(request, 'delete_news.html', context)
    elif request.method == 'POST':
        post.delete()
        return redirect('get-users')


@transaction.atomic
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('get-user-posts', post.user.pk)
    else:
        form = PostForm()
        return render(request, 'add_post.html', {'form': form})
