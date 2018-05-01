from django.urls import path
from . import views

app_name = 'foos'
urlpatterns = [
    # ex: /foos/
    path('', views.index, name='index'),
    # ex: /foos/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /foos/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /foos/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # ex: /foos/player/123/
    path('player/<int:player_id>/', views.player, name='player_profile'),
    # ex: /foos/singles/
    path('singles/', views.singles, name='singles_top'),
    # ex: /foos/doubles/
    path('doubles/', views.doubles, name='doubles_top'),
]

