from django.shortcuts import render
from django.views.generic import View 
from .forms import OrderCreateForm
from carrito.cart import Cart
from .models import OrderItem, Order 
from .tasks import order_created


# Create your views here.
class CreateOrder(View):
	def get(delf, request):
		form = OrderCreateForm()
		template_name = 'orders/create.html'
		context = {
		'form':form,
		'cart':Cart(request)
		}
		return render(request, template_name, context)

	def post(self, request):
		cart = Cart(request)
		form = OrderCreateForm(request.POST)
		if form.is_valid():
			order = form.save()
			for item in cart:
				OrderItem.objects.create(
					order=order,
					product=item['product'],
					price=item['price'],
					quantity=item['quantity']
					)
			#borrar carrito
			cart.clear()
			#enviaremos una tarea asíncrona a celery
			order_created.delay(order.id)
			template_name='orders/thanks.html'
			context = {
			'order':order
			}
			return render(request, template_name, context)

