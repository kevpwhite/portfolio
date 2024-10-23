from .models import Post, PostCategory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector

app_name='blog'

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'postsearch_list'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Post.objects.annotate(search=SearchVector('title', 'content')).filter(search=query)
        return Post.objects.none()
    
# Create your views here.    
class PostListView(ListView):
    model = Post
    context_object_name='posts'
    paginate_by = 6

    def get_queryset(self):
        return Post.objects.filter(status=1)

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories_list'] = PostCategory.objects.all()
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'  # Ensure you specify the correct template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the post object from the context
        post = self.object
        # Add the category to the context
        context['category'] = post.category  # Access the category directly from the post
        return context

class CategoriesView(ListView):
    model = Post
    template_name = 'blog/category_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        # Get the selected category based on the slug passed in the URL
        self.category = get_object_or_404(PostCategory, slug=self.kwargs['slug'])
        
        # Fetch all posts in this category and its child categories
        descendants = self.category.get_descendants(include_self=True)
        return Post.objects.filter(category__in=descendants)  

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        
        # Include the category in the context so you can display it in the template
        context['category'] = self.category
        
        # Optionally include child categories to display them
        context['child_categories'] = self.category.get_children()
        
        return context
