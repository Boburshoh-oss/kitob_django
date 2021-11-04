from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage,\
 PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 2
    template_name = 'list.html'
# def post_list(request):
#     object_list = Post.published.all()
#     paginator = Paginator(object_list, 3)
#     page = request.GET.get('page')
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
#     return render(request,'list.html',{'page': page,'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month, publish__day=day)

    return render(request,
    'detail.html',
    {'post': post})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
        else:
            form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
    'form': form})