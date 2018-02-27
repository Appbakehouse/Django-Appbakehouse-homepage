from django.conf.urls import url

from . import views
from bookmark.views import IndexView , DetailView

#app_name = 'bookmark'
urlpatterns = [

    # Class-based views for Bookmark app
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', DetailView.as_view(), name='detail'),
]