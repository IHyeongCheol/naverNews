import  urllib.request, bs4
import  pandas as pd
import re
from datetime import datetime
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from collections import Counter
from konlpy.tag import Okt
from PIL import Image
import numpy as np
from django import template

a = datetime.today().year        # 현재 연도 가져오기
b = datetime.today().month      # 현재 월 가져오기
c = datetime.today().day        # 현재 일 가져오기
date = datetime.today().strftime("%Y%m%d")     #yyyymmdd 형식으로
num = 100

#=================  정치 ======================
for i in range(0,6):
    url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=110'
    news_num = str(num + i)
    page = url + news_num
    for j in range(1,31):
        page = url + news_num + '&date=' + date + '&page=' + str(j)
        #print(page)

def politics():
    data = []
    # 크롤링
    for i in range(1,31):
        url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=100&date='
        page = url + date + '&page=' + str(i)
        web_page = urllib.request.urlopen(page)
        result = bs4.BeautifulSoup(web_page, 'html.parser')
        news_list = result.find(class_= "type06_headline")
        news = str(news_list.select('dt:nth-of-type(2) a'))
        newsText = re.compile('[가-힣]+').findall(news)
        data.append(newsText)

    # txt로 저장
    f = open("newsData.txt", 'w')
    f.write(str(data))
    f.close()
    #print(s)
    # 시각화 워드클라우드
    text = open('newsData.txt').read()
    okt = Okt()
    nouns = okt.nouns(text) # 명사만 추출
    words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

    c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
    wc = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(c)
    plt.figure()
    plt.imshow(gen)
    #plt.show()
    # 생성된 WordCloud를 politics.jpg로 보낸다.
    gen.to_file('../img/politics.jpg')
#politics()

#=================  정치 끝 ======================
#============================================
#=================  경제 =======================
def economy():
    data = []
    # 크롤링
    for i in range(1,31):
        url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=101&date='
        page = url + date + '&page=' + str(i)
        web_page = urllib.request.urlopen(page)
        result = bs4.BeautifulSoup(web_page, 'html.parser')
        news_list = result.find(class_= "type06_headline")
        news = str(news_list.select('dt:nth-of-type(2) a'))
        newsText = re.compile('[가-힣]+').findall(news)
        data.append(newsText)

    # txt로 저장
    f = open("economyData.txt", 'w')
    f.write(str(data))
    f.close()
    #print(s)
    # 시각화 워드클라우드
    text = open('economyData.txt').read()
    okt = Okt()
    nouns = okt.nouns(text) # 명사만 추출
    words = [n for n in nouns if len(n) > 1] # 단어의 길이가 1개인 것은 제외

    c = Counter(words) # 위에서 얻은 words를 처리하여 단어별 빈도수 형태의 딕셔너리 데이터를 구함
    wc = WordCloud(font_path='malgun', width=400, height=300, scale=2.0, max_font_size=250)
    gen = wc.generate_from_frequencies(c)
    plt.figure()
    plt.imshow(gen)
    #plt.show()
    # 생성된 WordCloud를 politics.jpg로 보낸다.
    gen.to_file('../img/economy.jpg')
#economy()
#=================  경제 끝 ======================
# i = 0
# for j in range(0,7):
#     i
#     aaa= str(int(date)-i)
#     url = 'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1=110'
#     if aaa[6:] == '00':
#         aaa = int(aaa)-69
#         date =str(aaa)
#         i = 0
#     i += 1
#     for n in range(1, 31):
#         page = url + '&date=' + str(aaa) + '&page=' + str(n)
#         print(page)


#  연합뉴스
i = 0
for j in range(0,7):
    i
    aaa= str(int(date)-i)
    url = 'https://news.naver.com/main/list.naver?mode=LPOD&sid2=140&sid1=001&mid=sec&oid=001&isYeonhapFlash=Y&date='
    if aaa[6:] == '00':
        aaa = int(aaa)-69
        date =str(aaa)
        i = 0
    i += 1
    for n in range(1, 31):
        page = url +  str(aaa) + '&page=' + str(n)
        print(page)