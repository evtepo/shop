from django.db import models


class Flowers(models.Model):
    title = models.CharField("Название", max_length=200)
    description = models.TextField("Описание")
    slug = models.SlugField("URL", max_length=200, unique=True, db_index=True)
    image = models.ImageField("Фото", upload_to="flowers/%Y/%m/%d/")
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    is_published = models.BooleanField("Публикация", default=False)
    category = models.ForeignKey("CategoriesForFlowers", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ...

    class Meta:
        verbose_name = "Цветок"
        verbose_name_plural = "Цветы"
        ordering = ["id", "title"]


class CategoriesForFlowers(models.Model):
    title = models.CharField("Названия категорий", max_length=200)
    slug = models.SlugField("URL", max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ...

    class Meta:
        verbose_name = "Категория цветов"
        verbose_name_plural = "Категории цветов"
        ordering = ["id", "title"]


class Other(models.Model):
    title = models.CharField("Название", max_length=200)
    slug = models.SlugField("URL", max_length=200, unique=True, db_index=True)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=6, decimal_places=2)
    image = models.ImageField("Фото", upload_to="others/%Y/%m/%d/")
    is_published = models.BooleanField("Публикация", default=False)
    category = models.ForeignKey("CategoriesForOthers", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ...

    class Meta:
        verbose_name = "Прочее"
        verbose_name_plural = "Прочее"
        ordering = ["id", "title"]


class CategoriesForOthers(models.Model):
    title = models.CharField("Прочее", max_length=200)
    slug = models.SlugField("URL", max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        ...

    class Meta:
        verbose_name = "Категория прочего"
        verbose_name_plural = "Категории прочего"
        ordering = ["id", "title"]
