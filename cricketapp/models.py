from django.db import models


class Team(models.Model):
    name=models.CharField(max_length=200)
    logo=models.ImageField(upload_to='media/')
    club_state=models.CharField(max_length=150)

    def __str__(self):
        return  self.name
class Player(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media1/')
    jersey_nmbr=models.IntegerField()
    country=models.CharField(max_length=150)
    matches=models.IntegerField()
    runs=models.IntegerField()
    high_score=models.IntegerField()
    fifties=models.IntegerField()
    hundres=models.IntegerField()
    player_type=models.CharField(max_length=250)

class Match(models.Model):
    date = models.DateField()
    time = models.TimeField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_one')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team_two')
    team1_score = models.IntegerField(max_length=50, null=True, blank=True)
    team2_score = models.IntegerField(max_length=50, null=True, blank=True)
    result = models.CharField(max_length=50, null=True, blank=True)







