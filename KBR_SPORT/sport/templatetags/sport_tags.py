from django import template
import sport.views as views
from sport.models import TagPost, Category

register = template.Library()

@register.inclusion_tag('sport_h/list_categories.html')
def show_category(cat_selected=None):
    cats = Category.objects.all()
    return {'cats': cats, 'cat_selected': cat_selected}


@register.inclusion_tag('sport_h/list_tags.html')
def show_all_tags():
    return {'tags': TagPost.objects.all()}