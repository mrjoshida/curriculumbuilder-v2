from django.conf.urls import patterns, url

from curricula import views

urlpatterns = patterns('curricula.views',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<slug>[-\w]+)/$', views.curriculum_view, name='curriculum_view'),
                       url(r'^(?P<slug>[-\w]+)/(?P<unit_slug>[-\w]+)/$', views.unit_view, name='unit_view'),
                       url(r'^(?P<slug>[-\w]+)/(?P<unit_slug>[-\w]+)/(?P<lesson_num>\d+)$', views.lesson_view, name='lesson_view'),
                       )