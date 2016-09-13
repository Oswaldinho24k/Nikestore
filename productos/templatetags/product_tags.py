from django import template 
register = template.Library()
from ..models import Category

@register.simple_tag
def categories():
	return Category.objects.all()