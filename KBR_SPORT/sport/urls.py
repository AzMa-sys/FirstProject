from django.urls import path, register_converter, include, re_path
from rest_framework.decorators import api_view
from rest_framework import routers

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from sport import views, converter, api_views
# from sport.api_views import SportViewSet
#
# register_converter(converter.FourDigitalConverter, 'year4')
#
# class MyCustomRouter(routers.SimpleRouter):
#     routes = [
#         routers.Route(url=r'^{prefix}/$',
#                       mapping={'get': 'list'},
#                       name='{basename}-list',
#                       detail=False,
#                       initkwargs={'suffix': 'list'}),
#         routers.Route(url=r'^{prefix}/{lookup}/$',
#                       mapping={'get': 'retrieve'},
#                       name='{basename}-detail',
#                       detail=True,
#                       initkwargs={'suffix': 'Detail'})
#     ]
#
# router = MyCustomRouter()
# router.register(r'sportlist', SportViewSet, basename='sportlist')

urlpatterns = [
    path('', views.SportHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('category/<slug:cat_slug>/', views.SportCategory.as_view(), name='category'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.SportPost.as_view(), name='post'),
    path('tag/<slug:tag_slug>/', views.SportTags.as_view(), name='tag'),
    path('addpage/', views.AddPage.as_view(), name='add'),
    path('edit/<slug:slug>/', views.UpdatePage.as_view(), name='edit_page'),
    path('del/<slug:slug>/', views.DeleteView.as_view(), name='del_page'),

    # path('api/v1/sportlist/', api_views.SportViewSet.as_view({'get': 'list'})),#DRF
    # path('api/v1/sportlist/<int:pk>/', api_views.SportViewSet.as_view({'put': 'update'})),
    # path('api/v1/', include(router.urls)),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/sportlist/', api_views.SportApiList.as_view()),#DRF
    path('api/v1/sportlist/<int:pk>/', api_views.SportApiUpdate.as_view()),

# JWT
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
