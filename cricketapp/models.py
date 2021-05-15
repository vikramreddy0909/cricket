from django.db import models


class Team_info(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    logo=models.ImageField(upload_to='media/')
    club_state=models.CharField(max_length=150)
class Playersinfo(models.Model):
    id=models.IntegerField(primary_key=True)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    image=models.ImageField(upload_to='media/')
    jersey_nmbr=models.IntegerField()
    counry=models.CharField(max_length=150)
    matches=models.IntegerField()
    runs=models.IntegerField()
    high_score=models.IntegerField()
    fifties=models.IntegerField()
    hundres=models.IntegerField()
    player_type=models.CharField(max_length=250)

class Matches_points(models.Model):
    team_matches=models.TextField(max_length=250)
    points=models.IntegerField()





