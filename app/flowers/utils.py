from datetime import datetime
from .models import Flowers
import random

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context['compositions'] = self.get_random_compositions(Flowers.objects.filter(category__title='Композиции', is_published=True).all())

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