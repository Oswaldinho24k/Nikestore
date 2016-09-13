from django.conf.urls import url
from . import views

urlpatterns = [

	
	url(r'^category/(?P<category>[-\w]+)/$', views.ListView.as_view(), name="category"),
	url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detalle'),
	url(r'^$', views.ListView.as_view(), name='products'),


]