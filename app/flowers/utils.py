from datetime import datetime
from .models import Flowers
import random

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['imported_flowers'] = Flowers.objects.all().filter(category__title='Привозные цветы', is_published=True)
        context['homemade'] = Flowers.objects.all().filter(category__title='Домашние цветы', is_published=True)
        context['soap'] = Flowers.objects.all().filter(category__title='Мыльные композиции', is_published=True)
        context['houseplants'] = Flowers.objects.all().filter(category__title='Комнатные растения', is_published=True)
        context['compositions'] = self.get_random_compositions(Flowers.objects.all().filter(category__title='Композиции', is_published=True))

        return context
    
    def get_random_compositions(self, obj):
        lst_of_comp = []

        while True:
            if len(lst_of_comp) == 6:
                break

            pk = random.randint(0, len(obj) - 1)
            if obj[pk] in lst_of_comp:
                continue

            lst_of_comp.append(obj[pk])

        return lst_of_comp