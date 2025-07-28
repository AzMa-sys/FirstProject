from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.db.transaction import commit
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import title
from django.template.loader import render_to_string
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.response import Response
from rest_framework.views import APIView

from KBR_SPORT.utils import DataMixin
from .form import AddFormPage, UploadFileForm
from .models import Sport, TagPost, Category, UploadFiles, Photos
from rest_framework import generics

from .serializers import SportSerializer


class SportHome(DataMixin, ListView):
    template_name = 'sport_h/index2.html'
    context_object_name = 'posts'
    title_page = 'Главная страница'
    cat_selected = 0

    def get_queryset(self):
        return Sport.published.all().select_related('cat')


@login_required
def about(request):
    about_list = Sport.published.all()
    paginator = Paginator(about_list, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'sport_h/about.html',
                  {'title': 'О сайте', 'page_obj': page_obj})


class SportPost(DataMixin, DetailView):

    template_name = 'sport_h/post.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return  self.get_mixin_context(context, title=context['post'].title)


    def get_object(self, queryset=None):
        return get_object_or_404(Sport.published, slug=self.kwargs[self.slug_url_kwarg])

class SportCategory(DataMixin, ListView):
    template_name = 'sport_h/index2.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sport.published.filter(cat__slug=self.kwargs['cat_slug']).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if context['posts']:
            cat = context['posts'][0].cat
            return self.get_mixin_context(context,
                                      title='Категория - '+ cat.name,
                                      cat_seleсted=cat.id)
        else:
            return self.get_mixin_context(context,
                                          title='Категория не найдена',
                                          cat_selected=0)


def contact(request):
    return HttpResponse(f'Обратная связь')

def login(request):
    return HttpResponse(f'Авторизация')

class AddPage(PermissionRequiredMixin, LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddFormPage
    template_name = 'sport_h/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Публикация'
    permission_required = 'sport.add_sport'

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


class UpdatePage(PermissionRequiredMixin, DataMixin, UpdateView):
    model = Sport
    fields = '__all__'
    template_name = 'sport_h/addpage.html'
    success_url = reverse_lazy('home')
    title_page = 'Редактирование'
    permission_required = 'sport.change_sport'


class DeletePage(DeleteView):
    model = Sport
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Sport.objects.delet

def page_not_found(request, exception):
    return HttpResponseNotFound('Страница не найдена')



class SportTags(DataMixin, ListView):
    template_name = 'sport_h/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Sport.published.filter(tags__slug=self.kwargs['tag_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = TagPost.objects.get(slug=self.kwargs['tag_slug'])
        return self.get_mixin_context(context,
                                      title='Тег - ' + tag.tag)

# DRF:

# class SportView(APIView):
#     def get(self, request):
#         lst = Sport.objects.all()
#         return Response({'posts': SportSerializer(lst, many=True).data})
#
#     def post(self, request):
#         serializer = SportSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'post': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT not allowed'})
#
#         try:
#             instance = Sport.objects.get(pk=pk)
#         except:
#             return Response({'error': 'Object does not exists'})
#         serializer = SportSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return serializer
