from datetime import datetime
from .models import Flowers

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['imported_flowers'] = Flowers.objects.all().filter(category__title='Привозные цветы', is_published=True)
        context['homemade'] = Flowers.objects.all().filter(category__title='Домашние цветы', is_published=True)
        context['soap'] = Flowers.objects.all().filter(category__title='Мыльные композиции', is_published=True)
        context['houseplants'] = Flowers.objects.all().filter(category__title='Комнатные растения', is_published=True)
        context['compositions'] = Flowers.objects.all().filter(category__title='Композиции', is_published=True)[:6]

        return context