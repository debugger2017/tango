from django.conf.urls import pattern,url
from rango import views

urlpatterns = patterns('',
				url(r'^$' , views.index , name = 'index')
				)