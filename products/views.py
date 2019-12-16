from django.shortcuts import render
from .models import Product, preciseCategory
from django.views.generic import ListView, DetailView, FormView, CreateView
from .forms import ProductForm

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', context={
        'products': products,
    })


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = preciseCategory.objects.all()
        return context

class ProductDetailView(DetailView):
    model = Product

"""
class ProductCreateView(FormView):
    form_class = ProductForm 
    success_url = '/products/product-list/'

    def form_valid(self, form):
        return super().form_valid(form)
    # pass
    # form.send_email()
    # return super().form_valid(form)
"""

class ProductCreateView(CreateView):
    model = Product
    fields = ['name', 'price', 'description', 'image', 'tags']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)