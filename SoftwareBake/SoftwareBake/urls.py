from django.conf.urls import include, url
from django.contrib import admin

from SoftwareBake.view import HomeView , UserCreateView, UserCreateDoneTV

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/register/$', UserCreateView.as_view(), name='register'),
    url(r'^accounts/register/done/$', UserCreateDoneTV.as_view(), name='register_done'),


    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^bookmark/', include('bookmark.urls')),
]