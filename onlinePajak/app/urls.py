from django.urls import path
from . import views

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('check_vendor/', views.GetVendor, name='check'),
    path('transaction/', views.transactionNumberView, name="transaction"),

    ]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])


