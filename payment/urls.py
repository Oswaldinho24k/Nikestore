
from django.conf.urls import url
from . import views

urlpatterns=[
	url(r'^conekta/$', views.Index.as_view(), name='conekta'),
	url(r'^process/$', views.PaymentProcess.as_view(),name='process'),
	url(r'^done/$',	views.payment_done, name="done"),
	url(r'^canceled/$',	views.payment_canceled,	name="canceled"),

]