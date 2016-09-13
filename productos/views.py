from django.shortcuts import render, get_object_or_404
from .models import Product, Category, Subcat
from django.views.generic import View
from carrito.forms import CartAddProductForm

# Create your views here.

class ListView(View):
	def get(self, request, category=None):
		#category=None
		if category:
			caty=Category.objects.get(category=category)
			products = Product.objects.all().filter(cat=caty)
		else:
			products = Product.objects.all()
		
		template_name='products/products.html'
		form=CartAddProductForm()
		cat=Category.objects.all()
		

		
		context={
		'products':products,
		'form':form,
		'caty':category,
		'cat':cat
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


		
