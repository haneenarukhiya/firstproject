from django.urls import path
from .import views
urlpatterns=[
path("my first page",views.homeview,name="fist"),
path("mysecondpage",views.second,name="second"),
path("extention", views.extention,name="extent"),
path("secondpage",views.homeview,name="second"),
path("secondpage2",views.second,name="second2"),
]