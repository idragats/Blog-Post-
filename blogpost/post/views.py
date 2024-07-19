from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Read posts
def post_list_view(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})



# Create post
@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user       
            post.save()                    
            return redirect('post_list')    
    else:
        form = PostForm()
    
    return render(request, 'post_form.html', {
        'form': form,
        'form_title': 'Ceate New Post',
        'button_text': 'Create Post'
    })

# Update post
@login_required
def post_update_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'post_form.html', {
        'form': form,
        'form_title': 'Update Post',
        'button_text': 'Update Post'
    })

# Delete post
@login_required
def post_delete_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('home')
    return render(request, 'post_confirm_delete.html', {'post': post})


#for search 

def search_results_view(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else Post.objects.all()
    return render(request, 'search_results.html', {'results': results, 'query': query})


def post_detail_view(request, post_id):
    post = get_object_or_404(Post, post_id=post_id) 
    return render(request, 'post_detail.html', {'post': post})