from .views import OrdersPageView
from django.urls import path

urlpatterns = [
    path('', OrdersPageView.as_view(), name='orders')
]