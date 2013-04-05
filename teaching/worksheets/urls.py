from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teaching.views.home', name='home'),

    url(r'^$', 'worksheets.views.home', name='home'),
)