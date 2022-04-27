# -*- coding: utf-8 -*-
"""python_crawler_0425.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uVFi-TuqZhZeN2QrSORjm0XlUC8_5Qb_

# 데이터 크롤링
> - 파이썬을 이용하여 웹상의 데이터를 모아보자.

우리는 매일 크롤러를 사용하고 있다.
> - 검색엔진(구글, 네이버)

### 웹 크롤링하는 의식의 흐름
> - 정보를 가져오고자 하는 url 정의
> - url정보로 requests로 정보 요청
> - text 정보를 html로 변환
> - html에서 우리가 필요한 정보만 선별

#### 셀렉터
> 용도 : html에서 내가 원하는 내용을 찾아내기 위해서  



```
<span class="news" id="1234">비비고 왕교자</span>
<span class="product" id="1235">비비고 볶음밥</span>
```



>> 단일 셀렉터 
``` 
html.select('span')  # 태그 이름이 span인 친구들을 다 들고옴  
```
tag : span  
class(별명, 그룹명) : .news

>> 클래스 포함 셀렉터
```
html.select('span.news') # 태그 이름이 span이고 class가 news인 것들을 불러옴.
```

>> id 포함 셀렉터
id(고유값) : #1234
```
html.select('span#1234') # 태그가 span이고 id가 1234인것들을 불러옴.
```

#### 복합 셀렉터
    1. 조합 셀렉터
    <span>1</span>
    <span class="txt">2</span>
    <em class="txt">3</em>
    
    태그 이름이 span이고 클래스 이름은 txt인 라인을 찾고 싶다. : span.txt 
    li 태그 중에서 id가 name 인 라인을 찾고\ 싶다. : li#name

    2. 경로 셀렉터
    
    <ul>
        <li><span>이걸 찾으려면?</span></li>
    </ul>
    <span>이건 아님</span>

    ul 태그안 li 태그 안 span 라인을 찾는다
    ul > li > span 혹은 ul li span

    html.select('ul li span')
    html.select('ul > li > span')
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from bs4 import BeautifulSoup

"""## 네이버 메인페이지 크롤링"""

url = 'https://www.naver.com/'
resp = requests.get(url)

resp.text # BeautifulSoup을 이용해 좀 더 보기 편하게 바꾸자.

html = BeautifulSoup(resp.text, 'html.parser')

"""> - 해당페이지의 이미지만 보고 싶다."""

img = html.select('img')
img # img tag로 된 모든 항목을 관측가능하다.

"""## 다음 뉴스페이지 크롤링"""

url = 'https://news.daum.net/'
resp = requests.get(url)
resp #<Response [200]>이면 제대로 된 것이다.

"""> - 100 우리 이런정보 내주는거야
> - 200 성공
> - 300 우리 이 사이트 이리루 이사했어 일루가
> - 400 유저가 요청을 잘못한경우
> - 500 서버 문제
"""

html = BeautifulSoup(resp.text, 'html.parser')
html.select('a.link_txt') # 리스트 형태로 반환되기 때문에 반복문, index를 통해 접근.

for title in html.select('a.link_txt')[:-13]:
    print(title.text.strip().replace('[', '').replace(']', ''))

"""## 로또 번호 가져오기"""

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EB%A1%9C%EB%98%90%EB%B2%88%ED%98%B8'

resp = requests.get(url)
resp

html = BeautifulSoup(resp.text, 'html.parser')

lotto_nums = []
for item in html.select('span.ball'):
    lotto_nums.append(int(item.text))

lotto_nums

"""### 여러회차 로또번호 가져오기
> - 페이지를 넘어가며 정보 수집.
> - 만들어진 정보를 df로 지정 및 csv파일로 저장.

>여러페이지를 한번에 크롤링 하는경우 서버에 요청을 다수하게되 차단이 일어날 수 있으므로 미리 난수를 만들어 코드 실행시간을 일정치 않게하여 사전에 차단을 예방한다. 


```
seed = np.random.randint(100)
np.random.seed(seed)
a = np.random.randint(5)
time.sleep(a)
```
"""

import time

lst = [i for i in range(1000, 1011)] # 1000 ~ 1010회차에 해당하는 로또 당첨번호를 크롤링해보자.
lotto_nums = []


for times in lst:

    seed = np.random.randint(100)
    np.random.seed(seed)
    a = np.random.randint(5)
    time.sleep(a)

    print(f'{times}회차 크롤링 중...')
    url = f'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query={times}%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8'
    resp = requests.get(url)
    html = BeautifulSoup(resp.text, 'html.parser')
    for elem in html.select('span.ball'):
        lotto_nums.append(int(elem.text))

# url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=1012%ED%9A%8C%20%EB%A1%9C%EB%98%90%EB%8B%B9%EC%B2%A8%EB%B2%88%ED%98%B8'

lotto_arr = np.array(lotto_nums).reshape(-1, 7) # numpy array를 이용해 shape을 각 회차에 맞게 바꾸어준다.

df = pd.DataFrame(data=lotto_arr, index=[f'{elem}회차' for elem in lst], columns=[i for i in range(1,7)] + ['보너스'])
df

df.to_csv('/content/drive/MyDrive/Colab Notebooks/이어드림스쿨/일자별 학습내용 정리/0425_python_crawler/data/lotto_nums.csv.gz')
## 만들어진 dataFrame을 csv형식(압축)으로 저장.

# 제대로 저장 되었는지 불러와서 확인해보자.

loaded_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/이어드림스쿨/일자별 학습내용 정리/0425_python_crawler/data/lotto_nums.csv.gz')
loaded_df

## 제대로 불러와지는것을 확인할 수 있다.

## 10회차에 걸쳐 어떤 번호가 많이 관측되었는지 그래프로 나타내보자.



plt.figure(figsize=(8, 6))

sns.countplot(lotto_nums)

plt.show()

"""## 네이버 키워드로 검색한 결과를 크롤링"""

search = input('검색어: ') # 검색어를 입력하고 그에 맞는 페이지에서 블로그 제목, 하이퍼링크를 크롤링. 


url = f'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query={search}'

resp = requests.get(url)
html = BeautifulSoup(resp.text, 'html.parser')

for elem in html.select('a.api_txt_lines.total_tit'):
    print(elem.text, ':', elem.attrs['href'])

"""## 관심있는 개별종목의 시가총액, 외국인 소진률, PER, PBR 가져오기"""

url = 'https://finance.naver.com/item/main.nhn?code=005930'
resp = requests.get(url)
html = BeautifulSoup(resp.text, 'html.parser')

시가총액 = html.select('tr.strong em')[0].text.replace('\t', '').replace('\n', '')
외국인소진률 = html.select('tr.strong em')[1].text
PER = html.select('em#_per')[0].text
PBR = html.select('em#_pbr')[0].text

"""## 여러종목의 시가총액, 외국인 소진률, PER, PBR 가져오기."""

stock_dict = {
    '삼성전자': '035720',
    '카카오': '005930',
    '현대차': '005380'
}

# 각 종목별 코드가 정해져있음.

stock_lst = []
index = []

for elem in stock_dict.values():

    seed = np.random.randint(100)
    np.random.seed(seed)
    a = np.random.randint(5)
    time.sleep(a)
    
    url = f'https://finance.naver.com/item/main.nhn?code={elem}'
    
    resp = requests.get(url)
    html = BeautifulSoup(resp.text, 'html.parser')

    index.append(html.select('h2 a')[0].text)
    stock_lst.append(html.select("em#_market_sum")[0].text.strip().replace('\t', '').replace('\n', ''))
    stock_lst.append(html.select('tr.strong td em')[1].text)
    stock_lst.append(html.select('em#_per')[0].text)
    stock_lst.append(html.select('em#_pbr')[0].text)

columns = ['시가총액', '외국인 소진률', 'PER', 'PBR']

stock_arr = np.array(stock_lst).reshape(-1, 4)

# dataFrame으로 만들기

df = pd.DataFrame(stock_arr, index=index, columns=columns)
df

# PER, PBR에 대하여 dtype을 변경해주자. (float64)

df['PER'] = df['PER'].astype('float64')
df['PBR'] = df['PBR'].astype('float64')

df.info()

# 마찬가지로 csv 파일로 저장 후 불러와보자.

df.to_csv('/content/drive/MyDrive/Colab Notebooks/이어드림스쿨/일자별 학습내용 정리/0425_python_crawler/data/stock.csv.gz')

loaded_df = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/이어드림스쿨/일자별 학습내용 정리/0425_python_crawler/data/stock.csv.gz')
loaded_df

#저장된 파일이 제대로 불러와짐을 볼수있다.

"""## 동적페이지 크롤링 (네이버 주식 시세)"""

# 동적페이지의 숨은 url
# 동적페이지에 요청을 할 때 웹 정책에 필요한 정보를 같이 전달해줘야함.
# requests 요청시 헤더정보 추가

url = 'https://finance.naver.com/item/sise_day.naver?code=005380&page=2'

info = {
    'referer': 'https://finance.naver.com/item/sise_day.naver?code=005380&page=1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

# 레퍼러정보 : 사용자가 이 페이지에 접속하기 전 어느 페이지에 있었는지
# 유저에이전트: 사용자컴퓨터 정보

resp = requests.get(url, headers=info) # 헤더에 위에서 정의한 info정보를 넣어줌.

html = BeautifulSoup(resp.text, 'html.parser')

index = [date.text for date in html.select('span.tah.p10')]
col_nm = [col.text for col in html.select('th')[1:]]
price = [num.text.strip() for num in html.select('span.tah.p11')]

price = np.array(price).reshape(-1, 6)
price

df = pd.DataFrame(price, index=index, columns=col_nm)
df

# 동적페이지의 경우에도 위와 같은 방식으로 접근해 데이터를 크롤링할 수 잇다.

# 종가에 대해 그래프로 그려 표현해보자
# dtype이 object이므로 int type으로 변환 후 진행해야한다.

def make_int(x):
    return x.replace(',', '')

df['종가'] = df['종가'].map(make_int)

df['종가'] = df['종가'].astype('int64')

df['종가']

plt.figure(figsize=(20, 6))

plt.plot(df['종가'].sort_index(ascending=True))

plt.show()

"""## 네이버 데이터랩 인기검색어 크롤링
> - json 데이터 파싱
"""

url = 'https://datalab.naver.com/shoppingInsight/getKeywordRank.naver?timeUnit=date&cid=50000000'

info = {
    'referer': 'https://datalab.naver.com/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}

resp = requests.post(url, headers=info)

resp.text

import json

data = json.loads(resp.text)
data

for item in data:
    print(item['datetime'], item['ranks'][0]['keyword'])

"""## API 활용

> - 파파고를 써보자
"""

url = 'https://openapi.naver.com/v1/papago/n2mt'

info = {
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Naver-Client-Id": "mEh9FgYD4uG4gmttEeG1",
    "X-Naver-Client-Secret": "g_8XOEMe23"
}

typing = input('한글: ')

data = {
    'source': 'ko',
    'target': 'en',
    'text': f'{typing}?'
}

resp = requests.post(url, headers=info, data=data)
trans = json.loads(resp.text)
trans['message']['result']['translatedText']


