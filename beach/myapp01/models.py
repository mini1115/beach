from datetime import datetime
from django.db import models

# Create your models here.

class Board(models.Model):
  writer=models.CharField(null=False,max_length=50)
  title=models.CharField(null=False,max_length=200)
  content=models.TextField(null=False)
  hit=models.IntegerField(default=0)
  post_date=models.DateTimeField(default=datetime.now,blank=True)
  filename=models.CharField(null=True,blank=True,default='',max_length=500)
  filesize=models.IntegerField(default=0)
  down=models.IntegerField(default=0)

  def hit_up(self):
    self.hit +=1

  def down_up(self):
    self.down += 1  

class Comment(models.Model):
  board = models.ForeignKey(Board, on_delete=models.CASCADE)
  writer=models.CharField(null=False, max_length=50)
  content=models.TextField(null=False)
  post_date=models.DateTimeField(default=datetime.now,blank=True)


# 지표
class sea_data(models.Model):
  date = models.CharField(null=False,max_length=50)
  #수온
  temp = models.CharField(null=False,max_length=50)
  #파고
  digging =models.CharField(null=False,max_length=50)
  wind_speed = models.CharField(null=False,max_length=50)
  air_temp = models.CharField(null=False,max_length=50)
  rainfall = models.CharField(null=False,max_length=50)


# 해수욕 지수
class sea_bathing_data(models.Model):
  date = models.CharField(null=False,max_length=50)
  #수온
  temp = models.CharField(null=False,max_length=50)
  #파고
  digging =models.CharField(null=False,max_length=50)
  wind_speed = models.CharField(null=False,max_length=50)
  air_temp = models.CharField(null=False,max_length=50)
  rainfall = models.CharField(null=False,max_length=50)
  #지수
  bathing = models.CharField(null=False,max_length=50)