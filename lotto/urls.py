from django.urls import include,path,re_path
from . import views


urlpatterns = [
re_path(r'^api/v1/saledatas/(?P<pk>[0-9]+)$',views.get_delete_update_sale.as_view(),name='get_delete_update_sale'),

path('api/v1/saledatas/',views.get_post_sale.as_view(),name='get_post_sale')

]