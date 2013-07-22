from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'game.views.index_page', name='index'),
    url(r'^game/', 'game.views.game_page', name='board'),
    
    url(r'^admin/', include(admin.site.urls)),
)
