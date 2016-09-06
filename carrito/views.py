from django.shortcuts import render, get_object_or_404, redirect
from .forms import CartAddProductForm
from django.views.generic import View
from .cart import Cart
from productos.models import Product


class AddProd(View):
	def post(self,request,product_id):
		cart = Cart(request)
		product = get_object_or_404(Product,id=product_id)
		form = CartAddProductForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			cart.add(product=product,
				quantity=cd['quantity'],
				update_quantity=cd['update'])
		return redirect('cart:cart_detail')

class Remove(View):
	def get(self,request,product_id):
		cart = Cart(request)
		product = get_object_or_404(Product,id=product_id)
		cart.remove(product)
		return redirect('cart:cart_detail')

class Detail(View):
	def get(self,request):
		cart = Cart(request)
		form = CartAddProductForm()
		context={
		'cart':cart,
		'form':form
		}
		return render(request,'cart/detail.html',context)





