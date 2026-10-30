from django.urls import path

from .views import home_page, detail_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('<slug:slug>/', detail_page, name='detail-page')
]
