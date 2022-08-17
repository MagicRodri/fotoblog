from atexit import register
from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def show(context,user):
    return user == context['user']