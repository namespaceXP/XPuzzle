from django.db import models

# Create your models here.

class User(models.Model):
    openid = models.CharField(max_length=40)
    name = models.CharField(max_length=40)
    score = models.IntegerField()
    mode = models.IntegerField()        #0为普通模式 1为游戏自动回复模式
    gameid = models.IntegerField()      #正在进行的游戏id
    gamenode = models.IntegerField()    #游戏目前的节点
    gameitem = models.IntegerField()    #拥有的道具

