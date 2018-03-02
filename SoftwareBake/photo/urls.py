from django.conf.urls import url

from photo.views import *

urlpatterns = [

    # Example: /
    url(r'^$', AlbumListView.as_view(), name='index'),

    # Example: /album/, same as /
    url(r'^album/$', AlbumListView.as_view(), name='album_list'),

    # Example: /album/99/
    url(r'^album/(?P<pk>\d+)/$', AlbumDetailView.as_view(), name='album_detail'),

    # Example: /photo/99/
    url(r'^photo/(?P<pk>\d+)/$', PhotoDetailViewV.as_view(), name='photo_detail'),
]

