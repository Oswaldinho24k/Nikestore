from django import template 
register = template.Library()
from django.contrib.auth.models import User


@register.simple_tag
def image_profile(request):

	social = request.user.social_auth.get(provider='facebook')
	return social.uid 