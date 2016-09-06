from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Subcat
from django.views.generic import View
from carrito.forms import CartAddProductForm

# Create your views here.

class ListView(View):
	def get(self, request):
		#if category:
		#	categories=Category.objects.get(name=categories)
		#	products = cat.product.all()
		#else:
		products = Product.objects.all()
		template_name='products/products.html'
		#products=Product.objects.all()

		context={
		'products':products,
		#'categories':categories
		}

		return render(request, template_name, context)

class DetailView(View):
	def get(self, request, slug):
		template_name='products/detail.html'
		product=get_object_or_404(Product, slug=slug)
		form=CartAddProductForm()

		context={
		'product':product,
		'form':form
		}

		return render(request, template_name, context)

