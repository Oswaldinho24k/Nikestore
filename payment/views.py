from django.shortcuts import render
from decimal import Decimal
from django.conf import settings
from django.core.urlresolvers import reverse
from django.shortcuts import render,get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from orders.models import Order
from django.views.generic import View
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt

class PaymentProcess(View):
	def get(self,request):
		order_id=request.session.get('order_id')
		order=get_object_or_404(Order,id=order_id)
		host=request.get_host()

		paypal_dict={
			'business':settings.PAYPAL_RECEIVER_EMAIL,
			'amount':'%.2f' % order.get_total_cost().quantize(Decimal('.01')),
			'item_name':'Order {}'.format(order.id),
			'invoice':str(order.id),
			'currency_code':'MXN',
			'notify_url':'http://{}{}'.format(host,reverse('paypal-ipn')),
			'return_url':'http://{}{}'.format(host,reverse('payment:done')),
			'cancel_return':'http://{}{}'.format(host,reverse('payment:canceled')),
		}
		form=PayPalPaymentsForm(initial=paypal_dict)
		return render(request,'payment/process.html',{'order':order,'form':form})

@csrf_exempt
def payment_done(request):
	order_id=request.session.get('order_id')
	order=get_object_or_404(Order,id=order_id)
	order.paid = True
	order.save()
	return render(request,'payment/done.html')

@csrf_exempt
def payment_canceled(request):
	return render(request,'payment/canceled.html')


from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect


#from payment.models import Sale
from django.conf import settings
import conekta

class Index(View):
	def get(self, request):
		order_id=request.session.get('order_id')
		order=get_object_or_404(Order,id=order_id)
		return render(request, 'charge.html')


	def post(self, request):
		
		conekta.api_key = settings.CONEKTA_PRIVATE_KEY

		order_id=request.session.get('order_id')
		#orden de db de django
		order=get_object_or_404(Order,id=order_id)
		amount = order.get_total_cost() * 100
		print(order.items.all()[0].product)
		
		#metodo para pago y orden en conekta
		order = conekta.Order.create({
			 
#
		    "line_items": [{
		        "name": "Compra total",
		        "unit_price": int(amount),
		        "quantity": 1
		   	}],
		    "shipping_lines": [{
		        #"amount": 1500,
		        "amount": 0,
		        "carrier": "mi compañia"
		    }],
		    "currency": "MXN",
		    "customer_info": {			    
			    #"name": "Mario Perez",
			    "name": order.first_name,
			    "email": order.email,
			    "phone": "7711732959"
			  },
		    "shipping_contact":{
		     "phone": "5555555555",
		     "receiver": "Bruce Wayne",
		     "address": {
		       "street1": "Calle 123 int 2 Col. Chida",
		       "city": "Cuahutemoc",
		       "state": "Ciudad de Mexico",
		       "country": "MX",
		       "postal_code": "06100",
		       "residential": True
		     }
		   },
		  "charges": [{
		        "payment_method":{
		          "type": "card",
		          "token_id": request.POST.get('conektaTokenId'),
		        } 
		        
		  }]
		})
				

		messages.success(request, 'siiiiiiii')
		return HttpResponse('ya pagaste bro!!')


