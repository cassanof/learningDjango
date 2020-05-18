from django.urls import path
from .views import (product_detail_view,
                    render_initial_data,
                    product_create_view,
                    dynamic_lookup_view,
                    product_nice_create_view,
                    product_delete_view,
                    product_list_view, )


app_name = "products"
urlpatterns = [
    path('<int:URLid>/', dynamic_lookup_view, name='products'),
    path('', product_list_view, name='list'),
    path('<int:URLid>/delete', product_delete_view, name='delete'),
    path('product/', product_detail_view, name='product'),
    path('create/', product_create_view, name='create'),
    path('nicecreate/', product_nice_create_view, name='nice_create'),
    path('render/', render_initial_data, name='render'),
]
