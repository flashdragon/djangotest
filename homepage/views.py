from django.shortcuts import HttpResponse, render
import random, json
import time
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib as plt
# Create your views here.
def home(request):
    return render(request,'home.html',)


def eda(request):
    # 다음 User-Agent를 추가해봅시다.
    frequency={}
    user_agent = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}
    for i in range(1,10):    
        res = requests.get("https://hashcode.co.kr/?page={}".format(i),user_agent)
        soup = BeautifulSoup(res.text,"html.parser")
        ul_tags = soup.find_all("ul","question-tags")
        for ul in ul_tags:
            li_tags=ul.find_all("li")
            for li in li_tags:
                tag=li.text.strip()
                if tag not in frequency:
                    frequency[tag]=1
                else:
                    frequency[tag]+=1
    counter=Counter(frequency)
    x = [elem[0] for elem in counter.most_common(10)]
    y = [elem[1] for elem in counter.most_common(10)]
    data={
        'columns':[x,y]
    }
    return HttpResponse(json.dumps(data),content_type='text/json')