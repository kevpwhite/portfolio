from .models import Category, Portfolio
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.postgres.search import SearchVector

app_name='portfolio'

class SearchResultsView(ListView):
    model = Portfolio
    template_name = 'portfolio/search.html'
    context_object_name = 'portfoliosearch_list'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Portfolio.objects.annotate(search=SearchVector('title', 'content')).filter(search=query)
        return Portfolio.objects.none()
    
    
    
# Create your views here.    
class PortfolioListView(ListView):
    model = Portfolio
    context_object_name ='portfolios'
    paginate_by = 9
    ordering = ['title']

    def get_context_data(self, **kwargs):
        context = super(PortfolioListView, self).get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        return context

class PortfolioDetailView(DetailView):
    model = Portfolio

    def get_context_data(self, **kwargs):
        #brings in the Portfolio model as self
        context = super(PortfolioDetailView,self).get_context_data(**kwargs)
        # filters portfolio model with the self cat id assigned
        catset = Portfolio.objects.all()
        # variable that stores queryset values for image and slug
        context['category_set'] = catset
        return context

class CategoriesView(ListView):
    model=Portfolio
    template_name='portfolio/category_list.html'
    context_object_name='categories'
    paginate_by = 6

    def get_queryset(self):
        self.category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return Portfolio.objects.filter(category=self.category)  

    def get_context_data(self, **kwargs):
        context = super(CategoriesView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context