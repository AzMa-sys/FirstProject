from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.db import models
from django.db.models import PROTECT
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Sport.Status.PUBLISHED)


class Sport(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Наименованиие товара')
    slug = models.SlugField(max_length=255, unique=True, db_index=True,
                            validators=[
                                MinLengthValidator(4, message='Минимум 5 символов'),
                                MaxLengthValidator(50, message='Максимум 50 символов')
                            ],verbose_name='Слаг товара')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото')
    content = models.TextField(blank=True, verbose_name='Основная информация')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)), default=Status.DRAFT, verbose_name='Статус публикациии')
    cat = models.ForeignKey('Category', on_delete=PROTECT, null=True, related_name='post', verbose_name='Категория')
    tags = models.ManyToManyField('TagPost', blank=True, related_name='tags', verbose_name='Теги')
    avail = models.OneToOneField('Avi', on_delete=models.SET_NULL, null=True, blank=True, related_name='avail',verbose_name='Статус товара')
    photos = models.ForeignKey('Photos', on_delete=models.SET_NULL, null=True, blank=True, related_name='photos')
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, related_name='posts', null=True, default=None)

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Наименованиие категории')
    slug = models.SlugField(max_length=255, db_index=True, verbose_name='Слаг категориии')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class TagPost(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug =models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse('tag', kwargs={'tag_slug': self.slug})


class Avi(models.Model):
    class Status(models.IntegerChoices):
        AVAILABLE = 1, 'В наличии'
        NOTAVAILABLE = 0, 'Нет в наличии'
        ORDER = 2, 'Можно заказать'

    status = models.CharField(max_length=100)
    count = models.IntegerField(null=True)

    def __str__(self):
        return self.status

class Photos(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name="Наименование изображения")
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото1')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото2')
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото3')
    photo4 = models.ImageField(upload_to='photos/%Y/%m/%d/', default=None,
                              blank=True, null=True, verbose_name='Фото4')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Изображения'

class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')