from django.shortcuts import render
from .models import Team_info,Playersinfo,Matches_points
from django.http import HttpResponseRedirect
from django.db import connection


def main(request):
    return render(request,'main.html')

def teamregister(request):
    return render(request,"registerteam.html")

def save_team_details(request):
    Team_info.objects.create(name=request.POST['name'],logo=request.POST['logo'],club_state=request.POST['clubstate'])
    return HttpResponseRedirect('/cricketapp/')
def display_teams(request):
    display=Team_info.objects.all()
    #cursor=connection.cursor()
    #cursor.execute('''select * from cricketapp_team_info''')
    #display=cursor.fetchall()
    return render(request,"displayteams.html",{'display':display})



# Create your views here.
