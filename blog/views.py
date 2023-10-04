from django.http import Http404
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import BlogPost, Category, Tag
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator


def blog(request):
    posts = BlogPost.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:3]
    popular_posts = BlogPost.objects.order_by('-views')[:3]

    # pagination 
    items_per_page = 4
    paginator = Paginator(posts, items_per_page)
    page_number = request.GET.get('page') # current page 
    page = paginator.get_page(page_number)

    context = {
        'posts': posts, 
        'categories': categories,
        'tags': tags,
        'recent_posts': recent_posts,
        'popular_posts': popular_posts,
        'page': page,
    }
    return render(request, 'blog/blog.html', context=context)

def blog_details(request, post_slug):
    if not request.session.get(f'viewed_{post_slug}'):  
        try:
            blog_post = get_object_or_404(BlogPost, slug=post_slug)
            
            # Increment the views count only if the user hasn't viewed it in this session
            # blog_post.views += 1
            # blog_post.save()
            
            # Mark the post as viewed in the current session
            request.session[f'viewed_{post_slug}'] = True
        except BlogPost.DoesNotExist:
            # Handle the case where the blog post does not exist
            raise Http404("Blog post does not exist")
    else:
        # If the post has already been viewed in this session, retrieve it without incrementing views
        blog_post = get_object_or_404(BlogPost, slug=post_slug)

    try:
        author_profile = blog_post.author.userprofile  
    except ObjectDoesNotExist:
        author_profile = None

    post_categories = blog_post.categories.all()
    categories = Category.objects.all()
    post_tags = blog_post.tags.all()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:3]
    popular_posts = BlogPost.objects.order_by('-views')[:3]
    recommended_posts = BlogPost.objects.filter(categories__in=post_categories).exclude(slug=post_slug).distinct().order_by('-publish_date')[:3]

    context = {
        'blog_post': blog_post, 
        'post_categories': post_categories, 
        'categories': categories,
        'post_tags': post_tags,
        'author_profile': author_profile,
        'recent_posts': recent_posts,
        'recommended_posts': recommended_posts,
        'popular_posts': popular_posts
    }

    return render(request, 'blog/blog_details.html', context=context)

def category_posts(request, category_slug):
    category = get_object_or_404(Category, name=category_slug)
    posts = BlogPost.objects.filter(categories=category)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:3]
    popular_posts = BlogPost.objects.order_by('-views')[:3]

    context = {
        'category': category,
        'posts': posts,
        'tags': tags,
        'categories': categories,
        'recent_posts': recent_posts,
        'popular_posts': popular_posts
    }
    
    return render(request, 'blog/category_posts.html', context=context)

def tag_posts(request, tag_slug):
    tag = get_object_or_404(Tag, name=tag_slug)
    posts = BlogPost.objects.filter(tags=tag)

    categories = Category.objects.all()
    tags = Tag.objects.all()
    recent_posts = BlogPost.objects.order_by('-publish_date')[:3]
    popular_posts = BlogPost.objects.order_by('-views')[:3]

    context = {
        'tag': tag,
        'posts': posts,
        'tags': tags,
        'categories': categories,
        'recent_posts': recent_posts,
        'popular_posts': popular_posts
    }
    
    return render(request, 'blog/taged_posts.html', context=context)
