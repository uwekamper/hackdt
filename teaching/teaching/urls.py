from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teaching.views.home', name='home'),
    url(r'^worksheets/', include('worksheets.urls')),
    url(r'^$', 'worksheets.views.index'),

    url(r'^overlord_webhook/$', 'worksheets.views.overlord_webhook'),
    url(r'^overlord/$', 'worksheets.views.overlord'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^login/$', 'worksheets.views.login'),

    url(r'oauth_callback/$', 'worksheets.views.oauth_callback', name='oauth_callback'),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'auth/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'auth/logout.html'}),
    #url(r'^accounts/register/$', 'teaching.views.register', {'template_name': 'auth/register.html'}),
)
