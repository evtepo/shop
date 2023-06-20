from datetime import datetime
from .models import Flowers

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['imported_flowers'] = Flowers.objects.all().filter(category__title='Привозные цветы')
        context['homemade'] = Flowers.objects.all().filter(category__title='Домашние цветы')
        context['soap'] = Flowers.objects.all().filter(category__title='Мыльные композиции')
        context['houseplants'] = Flowers.objects.all().filter(category__title='Комнатные растения')

        return context