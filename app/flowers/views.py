from typing import Any, Dict
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView

from .models import *
from .utils import DataMixin


class FlowersList(DataMixin, ListView):
    model = Flowers
    template_name = "flowers/base.html"
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context_from_mixin = self.get_user_context(title='Flowers')
        return dict(list(context.items()) + list(context_from_mixin.items()))

    def get_queryset(self):
        return Flowers.objects.all().select_related("category")
