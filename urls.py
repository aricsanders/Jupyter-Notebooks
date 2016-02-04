from django.conf.urls import url
from . import views
app_name= 'Files'
urlpatterns= [
  url(r'^$',views.index,name='index'),
  ]
