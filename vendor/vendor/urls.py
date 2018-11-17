from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'vendor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include([
        url(r'^truck/', include('truck.urls', namespace='account')),
    ])),
    url(r'^admin/', include(admin.site.urls)),
]
