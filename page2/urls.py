from django.urls import path
from . import views 

urlpatterns = [
    path("",views.store_page2_data,name='page2'),
]
