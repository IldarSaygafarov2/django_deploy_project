from django.template import Library

from test_app.models import Category


register = Library()


@register.simple_tag()
def show_categories():
    return Category.objects.all()
