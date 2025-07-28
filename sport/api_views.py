from django.core.serializers import serialize
from django.template.context_processors import request
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from sport.models import Sport, Category
from sport.serializers import SportSerializer
from rest_framework import generics, viewsets, mixins


# class SportViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    # mixins.UpdateModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     # queryset = Sport.objects.all()
#     serializer_class = SportSerializer
#
#     def get_queryset(self):
#         pk = self.kwargs.get('pk')
#
#         if not pk:
#              return Sport.objects.all()[:2]
#
#         return Sport.objects.filter(pk=pk)
#
#
#     @action(methods=['get'], detail=True)
#     def category(self, request, pk=None):
#         cats = Category.objects.get(pk=pk)
#         return Response({'cats': cats.name})


# class SportApiView(APIView):
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
#
#         serializer = SportSerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return serializer

class SportApiListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = "page_size"
    max_page_size = 10000

class SportApiList(generics.ListCreateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = SportApiListPagination

class SportApiUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer
    permission_classes = (IsAuthenticated, )


class SportRetrieveApiView(generics.RetrieveAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

class SportCRUDApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer