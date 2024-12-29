from django.urls import path
from . import views

urlpatterns = [
    path('account/', views.account, name='account'), #testing
    path('webhook/', views.webhook, name='webhook'),
]
