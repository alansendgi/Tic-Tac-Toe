from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

from games.models import Choice, Game


class IndexView(generic.ListView):
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
    p = get_object_or_404(Game, pk=game_id)
    
    selected_choice = p.choice_set.get(pk=request.POST['choice'])
    selected_choice.totals += 1

    if selected_choice.totals > 1:
        # Redisplay the game board.
        return render(request, 'games/detail.html', {
            'game': p,
            'error_message': "You must select an empty square.",
        })
    else:
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('games:results', args=(p.id,)))
