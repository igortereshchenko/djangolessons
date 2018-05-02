
from django.conf.urls import url
from mainpage import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^htmlload/', views.htmlload, name='htmlload'),
    url(r'^tryparams/', views.tryparameters, name='tryparameters'),
]
