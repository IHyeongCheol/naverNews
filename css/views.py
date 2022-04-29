import json

from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

from datetime import datetime
import  urllib.request, bs4
import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt

from css.errorcode import ErrorCode
from model.dao import userdao
from model.dao.sqlitedao import SqliteDao
from model.dao.userdao import UserDAO
from model.vo.uservo import UserVO


sqlitedao = SqliteDao('shop');
sqlitedao.makeTable();
userdao = UserDAO('shop');


def main(request):
    return render(request,'main.html');

def start(request):
    date = datetime.today().strftime("%Y%m%d")  #yyyymmdd 형식으로
    data = []
    data2 = []
    data3 = []
    data4 = []
    data5 = []
    data6 = []
    data7 = []
    data8 = []
    num = 100

    #크롤링
    for i in range(0, 6):
        url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1='
        news_num = str(num + i)
        page = url + news_num
        for j in range(1, 31):
            page = url + news_num + '&date=' + date + '&page=' + str(j)
            web_page = urllib.request.urlopen(page)
            result = bs4.BeautifulSoup(web_page, 'html.parser')
            news_list = result.find(class_="type06_headline")
            news = str(news_list.select('dt:nth-of-type(2) a'))
            newsText = re.compile('[가-힣]+').findall(news)
            if i == 0:
                data.append(newsText)
            if i == 1:
                data2.append(newsText)
            if i == 2:
                data3.append(newsText)
            if i == 3:
                data4.append(newsText)
            if i == 4:
                data5.append(newsText)
            if i == 5:
                data6.append(newsText)

# 오니피언
#     for i in range(1, 31):
#         url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=110'
#         page = url + '&date=' + date + '&page=' + str(i)
#         web_page = urllib.request.urlopen(page)
#         result = bs4.BeautifulSoup(web_page, 'html.parser')
#         news_list = result.find(class_="type06_headline")
#         news = str(news_list.select('dt:nth-of-type(2) a'))
#         newsText = re.compile('[가-힣]+').findall(news)
#         data7.append(newsText)

    i = 0
    for j in range(0, 7):
        i
        aaa = str(int(date) - i)
        url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=110'
        if aaa[6:] == '00':
            aaa = int(aaa) - 69
            date = str(aaa)
            i = 0
        i += 1
        for n in range(1, 31):
            page = url + '&date=' + str(aaa) + '&page=' + str(n)
            web_page = urllib.request.urlopen(page)
            result = bs4.BeautifulSoup(web_page, 'html.parser')
            news_list = result.find(class_="type06_headline")
            news = str(news_list.select('dt:nth-of-type(2) a'))
            newsText = re.compile('[가-힣]+').findall(news)
            data7.append(newsText)


#연합뉴스 속보
    # for i in range(1, 31):
    #     url = 'https://news.naver.com/main/list.naver?mode=LPOD&mid=sec&sid1=001&sid2=140&oid=001&isYeonhapFlash=Y'
    #     page = url + '&date=' + date + '&page=' + str(i)
    #     web_page = urllib.request.urlopen(page)
    #     result = bs4.BeautifulSoup(web_page, 'html.parser')
    #     news_list = result.find(class_="list_body newsflash_body")
    #     news = str(news_list.select('a'))
    #     newsText = re.compile('[가-힣]+').findall(news)
    #     data8.append(newsText)
    u = 0
    for j in range(0, 7):
        u
        aaa = str(int(date) - u)
        url = 'https://news.naver.com/main/list.naver?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date='
        if aaa[6:] == '00':
            aaa = int(aaa) - 69
            date = str(aaa)
            u = 0
        u += 1
        for n in range(1, 31):
            page = url + str(aaa) + '&page=' + str(n)
            web_page = urllib.request.urlopen(page)
            result = bs4.BeautifulSoup(web_page, 'html.parser')
            news_list = result.find(class_="list_body newsflash_body")
            news = str(news_list.select('a'))
            newsText = re.compile('[가-힣]+').findall(news)
            data8.append(newsText)


    # txt로 저장
    f = open("politicsData.txt", 'w')
    f2 = open("economyData.txt", 'w')
    f3 = open("societyData.txt", 'w')
    f4 = open("livingData.txt", 'w')
    f5 = open("worldData.txt", 'w')
    f6 = open("scienceData.txt", 'w')
    f7 = open("opinionData.txt", 'w')
    f8 = open("newsData.txt", 'w')

    f.write(str(data))
    f2.write(str(data2))
    f3.write(str(data3))
    f4.write(str(data4))
    f5.write(str(data5))
    f6.write(str(data6))
    f7.write(str(data7))
    f8.write(str(data8))

    f.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    # print(s)
    # 시각화 워드클라우드
    text = open('politicsData.txt').read()
    text2 = open('economyData.txt').read()
    text3 = open('societyData.txt').read()
    text4 = open('livingData.txt').read()
    text5 = open('worldData.txt').read()
    text6 = open('scienceData.txt').read()
    text7 = open('opinionData.txt').read()
    text8 = open('newsData.txt').read()

    okt = Okt()
    okt2 = Okt()
    okt3 = Okt()
    okt4 = Okt()
    okt5 = Okt()
    okt6 = Okt()
    okt7 = Okt()
    okt8 = Okt()

    nouns = okt.nouns(text)  # 명사만 추출
    nouns2 = okt2.nouns(text2)
    nouns3 = okt3.nouns(text3)
    nouns4 = okt4.nouns(text4)
    nouns5 = okt5.nouns(text5)
    nouns6 = okt6.nouns(text6)
    nouns7 = okt7.nouns(text7)
    nouns8 = okt8.nouns(text8)

    words = [n for n in nouns if len(n) > 1]  # 단어의 길이가 1개인 것은 제외
    words2 = [n for n in nouns2 if len(n) > 1]
    words3 = [n for n in nouns3 if len(n) > 1]
    words4 = [n for n in nouns4 if len(n) > 1]
    words5 = [n for n in nouns5 if len(n) > 1]
    words6 = [n for n in nouns6 if len(n) > 1]
    words7 = [n for n in nouns7 if len(n) > 1]
    words8 = [n for n in nouns8 if len(n) > 1]

    c = Counter(words)  # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
    c2 = Counter(words2)
    c3 = Counter(words3)
    c4 = Counter(words4)
    c5 = Counter(words5)
    c6 = Counter(words6)
    c7 = Counter(words7)
    c8 = Counter(words8)

    wc = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc2 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc3 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc4 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc5 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc6 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc7 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    wc8 = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)

    gen = wc.generate_from_frequencies(c)
    gen2 = wc2.generate_from_frequencies(c2)
    gen3 = wc3.generate_from_frequencies(c3)
    gen4 = wc4.generate_from_frequencies(c4)
    gen5 = wc5.generate_from_frequencies(c5)
    gen6 = wc6.generate_from_frequencies(c6)
    gen7 = wc7.generate_from_frequencies(c7)
    gen8 = wc8.generate_from_frequencies(c8)

    plt.figure()
    plt.imshow(gen)
    plt.imshow(gen2)
    plt.imshow(gen3)
    plt.imshow(gen4)
    plt.imshow(gen5)
    plt.imshow(gen6)
    plt.imshow(gen7)
    plt.imshow(gen8)
    # plt.show()
    # 생성된 WordCloud를 politics.jpg로 보낸다.
    gen.to_file('static/img/politics.jpg')
    gen2.to_file('static/img/economy.jpg')
    gen3.to_file('static/img/society.jpg')
    gen4.to_file('static/img/living.jpg')
    gen5.to_file('static/img/world.jpg')
    gen6.to_file('static/img/science.jpg')
    gen7.to_file('static/img/opinion.jpg')
    gen8.to_file('static/img/news.jpg')

    return render(request,'main.html');

#=========== 로그인 ==========

def logout(request):
    if request.session['sessionid'] != None:
        del request.session['sessionid'];
    return render(request, 'main.html');

def login(request):
    context = {
        'center':'login.html'
    };
    return render(request, 'login.html',context);

def loginimpl(request):
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    print(id, pwd);
    context = {};

    try:
        loginuser = userdao.select(id);
        if pwd == loginuser.getPwd():
            request.session['sessionid'] = id;
            context['center'] = 'main.html';
        else:
            raise Exception;
    except:
        context['center'] = 'main.html';

    return render(request, 'main.html',context);



def registerimpl(request):
    # ID,PWD,NAME
    id = request.POST['id'];
    pwd = request.POST['pwd'];
    name = request.POST['name'];

    user = UserVO(id,pwd,name);
    try:
        userdao.insert(user);
        context = {
            'center': 'main.html',
            'rname': name
        };
    except:
        context = {
            'center': 'error.html',
            'errorcode': ErrorCode.E0001
        };

    return render(request, 'registerOK.html',context);



def register(request):
    context = {
        'center':'register.html'
    };
    return render(request, 'register.html',context);

#=================  지도 ========
#14128726.5221587,       4516735.1981799
def location(request):
    data = {};
    #서울 37.55041692365908, 126.91037178013711
    data['lat'] = 37.55041692365908;
    data['lng'] = 126.91037178013711;
    data['positions'] = [
        {
            'content':'<h1>한국ICT인재개발원</h1>',
            'target':'http://www.naver.com',
            'lat': 14128726.5221587,
            'lng': 4516735.1981799
        },
    ];

    print(data);
    return HttpResponse(json.dumps(data), content_type='application/json');