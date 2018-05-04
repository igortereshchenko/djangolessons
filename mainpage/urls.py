
from django.conf.urls import url
from mainpage import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^htmlload/$', views.htmlload, name='htmlload'),
    url(r'^tryparams/$', views.tryparameters, name='tryparameters'),
    url(r'^form/$', views.formload, name='form'),
    url(r'^form_handler/$', views.form_handler, name='form_handler'),
    url(r'check_name/', views.check_name, name="check_name"),
]
