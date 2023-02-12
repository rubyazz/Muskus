from django.views.generic import DetailView
from django.views.generic import ListView
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def search(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        products = Product.objects.all()

    context = {
        'products': products,
        'query': query,
    }
    return render(request, 'search_results.html', context)

def home(request):
    return render(request, "home.html")


class ViewPost(DetailView):
   model = Product
   context_object_name = 'post'
   template_name = 'view_posts.html'

def men(request):
	a = Product.objects.filter(category_id='1')
	context = {'a': a}
	return render(request, 'men.html', context)


def uni(request):
	c = Product.objects.filter(category_id='3')
	context = {'c': c}
	return render(request, 'uni.html', context)

def women(request):
	b = Product.objects.filter(category_id='2')
	context = {'b': b}
	return render(request, 'women.html', context)