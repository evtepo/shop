from django.contrib import admin

from .models import *


class MainItemsMixin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "is_published", "category")
    list_display_links = ("id", "title")
    search_fields = ("title", "description")
    list_editable = ("is_published",)
    list_filter = ("is_published",)
    prepopulated_fields = {"slug": ("title",)}


class CategoryMixin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


class FlowersAdmin(MainItemsMixin):
    ...


class FlowersCategoriesAdmin(CategoryMixin):
    ...


class OtherAdmin(MainItemsMixin):
    ...


class OtherCategoriesAdmin(CategoryMixin):
    ...


admin.site.register(Flowers, FlowersAdmin)
admin.site.register(CategoriesForFlowers, FlowersCategoriesAdmin)
admin.site.register(Other, OtherAdmin)
admin.site.register(CategoriesForOthers, OtherCategoriesAdmin)
