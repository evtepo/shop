from django.views.generic import ListView

from datetime import date

from .models import *
from .utils import DataMixin


class FlowersList(DataMixin, ListView):
    model = Flowers
    template_name = "flowers/index.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_from_mixin = self.get_user_context(title='Flowers')
        return dict(list(context.items()) + list(context_from_mixin.items()))

    def get_queryset(self):
        return Flowers.objects.filter(is_published=True).select_related("category").all()


class CompositionsList(ListView):
    paginate_by = 6
    model = Flowers
    template_name = 'flowers/compositions.html'
    context_object_name = 'compositions'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Композиции'
        context['year'] = date.today().year
        return context
  
    def get_queryset(self):
        return Flowers.objects.filter(category__title='Композиции', is_published=True).all()