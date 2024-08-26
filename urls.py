from django.urls import path
from . import views
from .views import VendorUpdateView, VendorDeleteView

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('vendor/<int:vendor_id>/', views.vendor_detail, name='vendor_detail'),
    path('vendor/add/', views.add_vendor, name='add_vendor'),
    path('vendor/<int:pk>/update/', VendorUpdateView.as_view(), name='vendor_update'),
    path('vendor/<int:pk>/delete/', VendorDeleteView.as_view(), name='vendor_delete'),
    # Add more URLs for Contracts, Ratings, and Procurements as needed
]
