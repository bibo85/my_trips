from django.urls import path

from trips import views

urlpatterns = [
    path('', views.index, name='main_page')
]
