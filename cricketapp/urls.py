from django.urls import path
from . import views

urlpatterns =[
    path('',views.main,name='main'),
    path('display_teams/',views.display_teams,name='display_teams'),
    path('addplayer/',views.addplayer,name='addplayer'),
    path('save_player_details/',views.save_player_details,name='save_player_details'),
    path('<int:id>/players_details/',views.players_details,name='players_details'),
    path('<int:id>/player_info/',views.player_info,name='player_info'),
]






