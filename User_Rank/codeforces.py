import requests
import re
from bs4 import BeautifulSoup

def search(user_name):
    """
    user_name -> time_list, rank_list
    func:根据用户名列表查询用户排名变化
    """
    
    # idList=input('请以空格分隔输入id:').split()
    idList = [user_name]
    findRating=re.compile(r'">(.*?)</span> <span class="')
    findRank=re.compile(r'unrated.push(.*?);')
    findTime=re.compile(r'day=(.*?)&sec')
    time0=[]
    time1=[]
    time=[]
    rank0=[]
    rank=[]
    ids=[]
    times=[]
    ranks=[]
    for id in idList:
        try:
            url='https://codeforces.com/profile/'+id
            response=requests.get(url)
            response.encoding=response.apparent_encoding
            html1=response.text
            soup=BeautifulSoup(html1,'html.parser')
            rank0.append(re.findall(findRank,str(soup.find_all())))
            for i in rank0[0]:
                rank.append(str(i).split(',')[1])
            rank=rank[:len(rank)//6]
            time0.append(re.findall(findTime,str(soup.find_all())))
            time1=time0[0]
            time1=time1[:len(time1)//6]
            for t in time1:
                time.append(re.findall(r"\d+\.?\d*",t))#day,month,year,hour,min
            # print(id)
            ids.append(id)
            # print(rank)
            ranks.append(rank)
            # print(time)
            times.append(time)
            if len(rank) != 0 and len(time) != 0:
                return True, time, rank
            else:
                return False, [], []

        except:
            # print(f'未找到{id}')
            return False, [], []
