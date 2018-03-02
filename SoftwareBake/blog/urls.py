from django.conf.urls import url

from . import views
from blog.views import *

app_name = 'blog'
urlpatterns = [

    # Example: /
    url(r'^$', PostListView.as_view(), name='index'),

    # Example: /post/ (same as /)
    url(r'^post/$', PostListView.as_view(), name='post_list'),

    ## Example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name='post_detail'),

    # Example: /archive/
    url(r'^archive/$', PostArchiveIndexView.as_view(), name='post_archive'),

    # Example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYearArchiveView.as_view(), name='post_year_archive'),

    ## Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMonthArchiveView.as_view(), name='post_month_archive'),

    ## Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDayArchiveView.as_view(), name='post_day_archive'),

    ## Example: /today/
    url(r'^today/$', PostTodayArchiveView.as_view(), name='post_today_archive'),

    # Example: /tag/
    url(r'^tag/$', TagTemplateView.as_view(), name='tag_cloud'),  

    # Example: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTagTemplateView.as_view(), name='tagged_object_list'),

    # Example: /search/
    url (r'^search/$', SearchFormView.as_view(), name='search'),

    # Example: /add/
    url(r'^add/$',
        PostCreateView.as_view(), name="add",
    ),

    # Example: /change/
    url(r'^change/$',
        PostChangeLV.as_view(), name="change",
    ),

    # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        PostUpdateView.as_view(), name="update",
    ),

    # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        PostDeleteView.as_view(), name="delete",
    ),
]