from django.urls import path

from . import views

urlpatterns = [
    path('', views.greetings, name='greetings'),
    path('items/', views.list_item, name='items'),
    path('shop/<int:id>/', views.detail_item, name='detail'),
]

