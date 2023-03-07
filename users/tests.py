from django.test import TestCase
from .views import SignUpPageView

urlpatterns = [
    path('signup', SignUpPageView.as_view(), name='signup'),
]