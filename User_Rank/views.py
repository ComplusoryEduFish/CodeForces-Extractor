from calendar import month
from distutils.log import error
import json
from time import time
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic
from .models import User, Rank
from .codeforces import search

FOUND = False
SHOWN = False
error_text = None


def index(request):
    global FOUND, SHOWN, error_text
    if not FOUND and error_text:# 查询失败信息仅显示一次
        if SHOWN:
            SHOWN = False
            error_text = None
        else:
            SHOWN = True

    if request.method == 'POST':
        # 重置，读取
        User.objects.all().delete()
        user_name = request.POST['user_name']
        FOUND, time_list, rank_list = search(user_name)
        SHOWN = False

        # 存储，跳转
        if FOUND == True:
            User.objects.create(user_name=user_name) # 创建用户
            for i in range(len(time_list)): # 逐条创建用户排名信息
                Rank.objects.create(user=User.objects.filter(user_name=user_name)[0], 
                    score=rank_list[i], year=time_list[i][2], month=time_list[i][1], day=time_list[i][0])
            error_text = None
            return HttpResponseRedirect(reverse('User_Rank:rank', args=()))
        else:
            error_text = '该用户不存在！'
            return HttpResponseRedirect(reverse('User_Rank:index', args=()))
        
    return render(request, 'User_Rank/index.html', {'error_text':error_text, 'FOUND':FOUND})


def rank(request):
    rank_set = list(Rank.objects.all())
    xlist = [int(rank.score) for rank in rank_set]
    ylist = [str(rank.year)+'年'+str(rank.month)+'月'+str(rank.day)+'日' for rank in rank_set]
    content = {'xlist':json.dumps(xlist), 'ylist':json.dumps(ylist), 'user_name':User.objects.all()[0].user_name}
    return render(request, 'User_Rank/rank.html', content)