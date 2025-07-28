from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Sport, Category, Avi, Photos


class AviFilter(admin.SimpleListFilter):
    title = 'Наличие'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return [
            ('Not availability', 'Нет в наличии'),
            ('Availability', 'В наличии'),
            ('Order', 'Можно заказать')
        ]

    def queryset(self, request, queryset):
        if self.value() == 'Not availability':
            return queryset.filter(avail=0)
        elif self.value() == 'Availability':
            return queryset.filter(avail=1)
        elif self.value() == 'Order':
            return queryset.filter(avail=2)

@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content','post_photo', 'photo', 'photos', 'is_published', 'cat', 'tags', 'avail']
    readonly_fields = ['post_photo']
    prepopulated_fields = {'slug': ('title', )}
    filter_horizontal = ['tags']
    list_display = ('id', 'title','post_photo', 'time_create', 'is_published')
    list_display_links = ('id', 'title' )
    ordering = ['time_create',  'title']
    list_editable = ('is_published', )
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = [AviFilter, 'cat__name', 'is_published', 'photos__name']
    save_on_top = True

    @admin.action(description='Опубликовать')
    def set_published(self, request, querytest):
        count = querytest.update(is_published=Sport.Status.PUBLISHED)
        self.message_user(request, f'Опуликованно {count} публикации')

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, querytest):
        count = querytest.update(is_published=Sport.Status.DRAFT)
        self.message_user(request, f'{count} снято с публикации', messages.WARNING)

    @admin.display(description='Изображение')
    def post_photo(self, sport: Sport):
        if sport.photo:
            return mark_safe(f'<img src="{sport.photo.url}" width=200>')
        return 'Без Фото'

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

@admin.register(Avi)
class AviAdmin(admin.ModelAdmin):
    list_display = ('id', 'status', 'count')
    list_editable = ('status', 'count')

@admin.register(Photos)
class PhotosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'post_photo1','post_photo2', 'post_photo3', 'post_photo4')
    list_display_links  = ('id', 'name')

    @admin.display(description='Изображение')
    def post_photo1(self, photo: Photos):
        if photo.photo1:
            return mark_safe(f'<img src="{photo.photo1.url}" width=200>')
        return 'Без Фото'

    @admin.display(description='Изображение')
    def post_photo2(self, photo: Photos):
        if photo.photo2:
            return mark_safe(f'<img src="{photo.photo2.url}" width=200>')
        return 'Без Фото'

    @admin.display(description='Изображение')
    def post_photo3(self, photo: Photos):
        if photo.photo3:
            return mark_safe(f'<img src="{photo.photo3.url}" width=200>')
        return 'Без Фото'

    @admin.display(description='Изображение')
    def post_photo4(self, photo: Photos):
        if photo.photo4:
            return mark_safe(f'<img src="{photo.photo4.url}" width=200>')
        return 'Без Фото'