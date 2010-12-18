from django.conf.urls.defaults import *

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^outyet/', include('outyet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^tools/trustedurl/(?P<url>.*)', 'watchlists.views.trusted_url'),
    (r'^addentry', 'watchlists.views.addentry'),
    (r'^login/', 'watchlists.views.login'),
    (r'^admin/', include(admin.site.urls))
    
)
