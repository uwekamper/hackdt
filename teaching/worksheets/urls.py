from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'teaching.views.home', name='home'),

    #url(r'^$', 'worksheets.views.home', name='home'),
    url(r'^teachers/$', views.TeacherList.as_view()),
    url(r'^teachers/(?P<slug>[a-zA-Z0-9]+)/$', views.TeacherDetails.as_view()),
    url(r'^teachers/(?P<slug>[a-zA-Z0-9]+)/student_groups/$', views.TeacherDetails.as_view()),

    url(r'^students/$', views.StudentList.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.StudentDetails.as_view()),
)