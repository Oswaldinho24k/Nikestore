"""nikestore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf import settings
from django.views.static import serve
from django.contrib import admin
from productos import urls as productUrls
from carrito import urls as cartUrls
from orders import urls as orderUrls
from paypal.standard.ipn import urls as paypalUrls
from payment import urls as paymentUrls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cart/', include(cartUrls, namespace="cart")),
    url(r'^products/',include(productUrls, namespace='products')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view=serve,
        kwargs={'document_root':settings.MEDIA_ROOT}),

    
    url(r'^orders/', include(orderUrls, namespace="orders")),
    url(r'^paypal/', include(paypalUrls)),
    url(r'^payment/', include(paymentUrls,namespace='payment')),

]
