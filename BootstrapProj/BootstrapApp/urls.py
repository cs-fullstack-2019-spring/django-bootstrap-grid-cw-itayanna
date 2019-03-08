from django.urls import path
from . import views


# this establishes the url pathways and connects them to the view functions

urlpatterns = [
    path('', views.index, name='index'),
    path('page2/', views.page2, name='page2'),
    path('page2/page3/', views.page3, name='page3')
]