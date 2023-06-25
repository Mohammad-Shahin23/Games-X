from django.shortcuts import render

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Game

class GameListView(ListView):
    template_name = 'Game/Game-list.html'
    model = Game

class GameDetailView(DetailView):
    template_name = 'Game/Game-detail.html'
    model = Game

class GameCreateView(CreateView):
    template_name = 'Game/Game-create.html'
    model = Game
    fields = [ 'Game', 'player', 'Consel', 'Discription']

class GameUpdateView(UpdateView):
    template_name = 'Game/Game-update.html'
    model = Game
    fields = ['Game', 'player', 'Consel', 'Discription']

class GameDeleteView(DeleteView):
    template_name = 'Game/Game-delete.html'
    model = Game
    success_url = reverse_lazy('Game_list')