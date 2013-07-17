from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'game.views.index_page', name='index'),
    url(r'^about/', 'game.views.about_page', name='about'),
    url(r'^game/', 'game.views.game_page', name='game'),

    url(r'^admin/', include(admin.site.urls)),
)
