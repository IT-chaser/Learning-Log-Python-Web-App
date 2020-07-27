from django.shortcuts import render, redirect

from .models import BlogPost
from .forms import BlogForm

def index(request):
    """The home page for blogs."""
    return render(request, 'blogs/index.html')

def blogs(request):
    """Show all blogs."""
    blogs = BlogPost.objects.order_by('date_added')
    context = {'blogs': blogs}
    return render(request, 'blogs/blogs.html', context)

def blog(request, blog_id):
    """Show a single blog and its entries."""
    blog = BlogPost.objects.get(id=blog_id)
    entries = blog.entry_set.order_by('-date_added')
    context = {'blog': blog, 'entries': entries}
    return render(request, 'blogs/blog.html', context)

def new_post(request):
    """Add a new post."""
    if request.method != 'POST':
        # No data submitted: create a blank form.
        form = BlogForm()
    else:
        # POST data submitted: process data.
        form = BlogForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)

def edit_post(request, post_id):
    """Edit an existing post."""
    post = BlogPost.objects.get(id=post_id)
    blog = post.blogs

    if request.method != 'POST':
        # Initial request: pre-fill form with the current entry.
        form = BlogForm(instance=post)
    else:
        # POST data submitted; process data.
        form = BlogForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:blogs', post_id=post.id)

    context = {'post': post, 'blog': blog, 'form': form}
    return render(request, 'blogs/edit_post.html', context)
