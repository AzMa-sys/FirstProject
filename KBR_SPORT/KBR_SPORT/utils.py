menu = [
    {'title': 'Главная страница', 'url_name': 'home'},
    {'title': 'О нас', 'url_name': 'about'},
    {'title': 'Обратная связь', 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 10
    title_page = None
    extra_context = {}
    cat_selected = None
    y = [1, 2, 3, 4]



    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected


    def get_mixin_context(self, context, **kwargs):
        context['cat_selected'] = None
        context.update(kwargs)
        return context