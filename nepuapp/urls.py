from django.conf.urls import url
from .import views

app_name = 'nepuapp'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/$', views.news, name='news'),
    #url(r'^static/$', views.static, name='static'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]