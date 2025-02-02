from django.urls import path
from . import views

urlpatterns = [
    path('',views.store_page3_data,name='page3'),
]
