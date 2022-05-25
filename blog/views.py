from .models import Post, PostCategory
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# from django.contrib.postgres.search import SearchVector
from django.shortcuts import get_object_or_404

app_name='blog'

class SearchResultsView(ListView):
    model = Post
    template_name = 'blog/search.html'
    context_object_name = 'postsearch_list'
    paginate_by = 6

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.annotate(search = SearchVector('title', 'content'),).filter(search=query)
        return object_list
    
# Create your views here.    
class PostListView(ListView):
    model = Post
    context_object_name='posts'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['categories_list'] = PostCategory.objects.all()
        return context

    #OLD CATEGORY SET
    # def get_context_data(self, **kwargs):
    #     #brings in the Portfolio model as self
    #     context = super(PostListView,self).get_context_data(**kwargs)
    #     # filters portfolio model with the self cat id assigned
    #     catset = Post.objects.filter(status=1)
    #     # variable that stores queryset values for image and slug
    #     context['category_set'] = catset
    #     return context

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        #brings in the Portfolio model as self
        context = super(PostDetailView,self).get_context_data(**kwargs)
        # filters portfolio model with the self cat id assigned
        catset = Post.objects.all()
        # variable that stores queryset values for image and slug
        context['category_set'] = catset
        return context

class CategoriesView(ListView):
    model = Post
    template_name='blog/category_list.html'
    context_object_name='categories'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(PostCategory, slug=self.kwargs['slug'])
        return Post.objects.filter(category=self.category)  

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context