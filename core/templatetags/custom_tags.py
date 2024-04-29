from django.template import Library
from core.models import Collection

register = Library()

@register.simple_tag()
def get_collections():
    return Collection.objects.all()
