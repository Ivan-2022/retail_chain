from django.urls import path

from .views import FactoryCreateView, FactoryListView, FactoryView, RetailCreateView, RetailListView, RetailView, \
    EntrepreneurCreateView, EntrepreneurListView, EntrepreneurView, ContactCreateView, ContactListView, ContactView, \
    ProductCreateView, ProductListView, ProductView, FactoryUpdateView, FactoryDeleteView, RetailUpdateView, \
    RetailDeleteView, EntrepreneurUpdateView, EntrepreneurDeleteView

urlpatterns = [
    path('factory/create', FactoryCreateView.as_view(), name='factory_create'),
    path('factory/list', FactoryListView.as_view(), name='factory_list'),
    path('factory/<pk>', FactoryView.as_view(), name='factory'),
    path('factory/update/<pk>', FactoryUpdateView.as_view(), name='factory_update'),
    path('factory/delete/<pk>', FactoryDeleteView.as_view(), name='factory_delete'),
    path('retail/create', RetailCreateView.as_view(), name='retail_create'),
    path('retail/list', RetailListView.as_view(), name='retail_list'),
    path('retail/<pk>', RetailView.as_view(), name='retail'),
    path('retail/update/<pk>', RetailUpdateView.as_view(), name='retail_update'),
    path('retail/delete/<pk>', RetailDeleteView.as_view(), name='retail_delete'),
    path('entrepreneur/create', EntrepreneurCreateView.as_view(), name='entrepreneur_create'),
    path('entrepreneur/list', EntrepreneurListView.as_view(), name='entrepreneur_list'),
    path('entrepreneur/<pk>', EntrepreneurView.as_view(), name='entrepreneur'),
    path('entrepreneur/update/<pk>', EntrepreneurUpdateView.as_view(), name='entrepreneur_update'),
    path('entrepreneur/delete/<pk>', EntrepreneurDeleteView.as_view(), name='entrepreneur_delete'),
    path('contact/create', ContactCreateView.as_view(), name='contact_create'),
    path('contact/list', ContactListView.as_view(), name='contact_list'),
    path('contact/<pk>', ContactView.as_view(), name='contact'),
    path('product/create', ProductCreateView.as_view(), name='product_create'),
    path('product/list', ProductListView.as_view(), name='product_list'),
    path('product/<pk>', ProductView.as_view(), name='product'),
]
