from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from .forms import PlayersForm
from .models import Team,Player,Match


def main(request):
    return render(request, 'main.html')


def display_teams(request):
    # display=Team.objects.all()
    cursor = connection.cursor()
    cursor.execute('''select * from cricketapp_team''')
    display = cursor.fetchall()
    return render(request, "displayteams.html", {'display': display})


def addplayer(request):
    cursor = connection.cursor()
    cursor.execute('''select * from cricketapp_team''')
    addplayer = cursor.fetchall()
    form=PlayersForm()
    return render(request, "playersinfo.html", {'form':form,'display': addplayer})


def save_player_details(request):
    if request.method == 'POST':
        form_obj = PlayersForm(request.POST, request.FILES)
        if form_obj.is_valid():
            form_obj.save()
        return HttpResponseRedirect('/cricketapp/')

    return HttpResponseRedirect('/cricketapp/')


def players_details(request,id):
    #details1 = Player.objects.get(id=id)
    cursor=connection.cursor()
    cursor.execute(f'''select * from cricketapp_team
    join cricketapp_player on cricketapp_team.id=cricketapp_player.team_id
    where cricketapp_team.id={id}''')
    details1=cursor.fetchall()
    return render(request, 'playerslist.html',{'details':details1})

def player_info(request,id):
    details=Player.objects.get(id=id)
    return render(request,'playerdetails.html',{'details':details})

# Create your views here.
