"""
    Master URL Pattern List for the application.  Most of the patterns here should be top-level
    pass-offs to sub-modules, who will have their own urls.py defining actions within.
"""

# pylint: disable=W0401, W0614
from django.conf.urls import *  #@UnusedWildImport
from django.contrib import admin
from django.conf import settings
from views import IndexView, SecureView
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns('',

    # Home Page
    url(r'^$', never_cache(IndexView.as_view()), name="sp_demo_home_page"),

    # Secure Page
    url(r'^secure/$', never_cache((login_required(SecureView.as_view()))), name="sp_demo_secure_page"),

    # Secure Page Too
    url(r'^securetoo/$', never_cache(login_required(SecureView.as_view(template_name="securetoo.html"))), name="sp_demo_secure_page_too"),

    # Social Profiles
    url(r'^socialprofile/', include('socialprofile.urls')),
    
    # Admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin Site:
    (r'^admin/', include(admin.site.urls)),

    # Robots and Favicon
    (r'^robots\.txt$', 'django.views.generic.simple.direct_to_template', {'template': 'robots.txt', 'mimetype': 'text/plain'}),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': settings.STATIC_URL + 'images/favicon.ico'}),
)