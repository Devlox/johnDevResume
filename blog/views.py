from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Post, Category

def index(request):
    queryset = Post.objects.order_by('-timestamp').filter(is_published=True)

    paginator = Paginator(queryset, 6)
    page = request.GET.get('page')
    paged_queryset = paginator.get_page(page)

    context = {
        'posts_list': paged_queryset
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, slug_text):
    queryset = get_object_or_404(Post, slug = slug_text)

    context = {
        'post_details': queryset
    }

    return render(request, 'blog/post.html', context)

def post_category_list(request, cat_slug):
    categories = Category.objects.all()
    post = Post.objects.order_by('-timestamp').filter(is_published=True)
    if cat_slug:
        category = get_object_or_404(Category, cat_slug=cat_slug)
        post = post.filter(categories = category)
    
    context = {
        'categories': categories,
        'post': post,
        'category': category
    }

    return render(request, 'blog/posts_cat_list.html', context)
