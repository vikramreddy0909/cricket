from django.urls import path
from . import views

urlpatterns =[
    path('',views.main,name='main'),
    path('display_teams/',views.display_teams,name='display_teams'),
    path('teamregister/',views.teamregister,name='teamregister'),
    path('save_team_details/',views.save_team_details,name='save_team_details'),
]