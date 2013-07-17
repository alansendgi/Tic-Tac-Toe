from django.shortcuts import render

def index_page(request):
	return render(request, 'game/index.html', {})

def game_page(request):
    return render(request, 'game/game.html', {})
    
def about_page(request):
    return render(request, 'game/about.html', {})