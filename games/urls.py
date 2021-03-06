from django.conf.urls import patterns, url

from games import views

urlpatterns = patterns('',
    url(r'^$',
        views.IndexView.as_view(),
        name='index'),
    
    url(r'^(?P<pk>\d+)/$',
        views.DetailView.as_view(),
        name='detail'),
    
    url(r'^(?P<pk>\d+)/results/$',
        views.ResultsView.as_view(),
        name='results'),
    
    url(r'^(?P<game_id>\d+)/play/$',
        views.play,
        name='play'),
    
    url(r'^(?P<game_id>\d+)/reset/$',
        'game_reset',
        name='games_game_reset'),
)
