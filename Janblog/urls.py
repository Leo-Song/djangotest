from django.contrib import admin
from django.urls import path, re_path
from Janblog import views

app_name = 'Janblog'
#test
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(),name='index'),
    # path('', views.index, name='index'),
    # re_path('^search/$',views.search, name='search'),
    re_path('^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail'),
    re_path('^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.ArchivesView.as_view(), name='archives'),
    re_path('^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='category'),
]
