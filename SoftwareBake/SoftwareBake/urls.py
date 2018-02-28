from django.conf.urls import include, url
from django.contrib import admin

from SoftwareBake.view import HomeView

urlpatterns = [
    
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^blog/', include('blog.urls')),
    url(r'^bookmark/', include('bookmark.urls')),
]