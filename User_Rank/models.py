from calendar import month
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=200, help_text='用户名')
    
    def __str__(self):
        return self.user_name

class Rank(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(help_text='排名数')
    year = models.IntegerField(help_text='排名对应年')
    month = models.IntegerField(help_text='排名对应月')
    day = models.IntegerField(help_text='排名对应日')

    def __str__(self):
        return str(self.score)
