from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from games.models import Board, Choice, Game
"""
see https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/#model-style
for ideas
"""

class IndexView(generic.ListView):
    """
    Still contains left-overs from the 'Polls' tutorial
    """
    template_name = 'games/index.html'
    context_object_name = 'latest_game_list'

    def get_queryset(self):
        """
        Return the last five games.
        """
        return Game.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    """
    Still contains left-overs from the 'Polls' tutorial, 
    but I adapted them to make this app work.
    """
    model = Game
    template_name = 'games/detail.html'
    
    def get_queryset(self):
        """
        Excludes any games that aren't published yet.
        """
        return Game.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Game
    template_name = 'games/results.html'


def play(request, game_id):
    """
    Needs work
    """
    
    p = get_object_or_404(Game, pk=game_id)
    """get the game_id for Game"""
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
    selected_choice.totals += 1
    selected_choice.save()

#    if selected_choice.totals > 1:
#        # Redisplay the game board.
#        return render(request, 'games/detail.html', {
#            'game': p,
#            'error_message': "You must select a free square.",
#        })
#    else:

    return render(request, 'games/detail.html', {
        'game': p,
        'error_message': "You selected square number %s" % selected_choice,
    })
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse('games:results', args=(p.id,)))
