from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def model_type(instance):
    return instance.__class__.__name__

@register.simple_tag(takes_context=True)
def name_display(context,user):
    if user == context['user']:
        return 'you'
    return user.username

@register.filter
def instance_timestamp_display(time):
    current_time = timezone.now()
    difference = current_time - time # datetime.timedelta
    time_str = ''
    if difference.days > 0: # difference > 24h
        time_str = f"at {time.strftime('%H:%M %d %b %Y')}"
    else:
        h = difference.seconds // (60*60)  
        m = difference.seconds // 60
        if 1 <= h < 24 : # difference within 24h
            time_str = f"{h} hours ago"
        elif 0 < m < 60: # difference within 60min
            time_str = f"{m} minutes ago"
        else :
            time_str = f"just now"

    return time_str
