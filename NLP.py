#!/usr/bin/env python
# coding: utf-8

# # 16.1 자연어 처리가 필요한 상황
# - 주어진 데이터가 문자열이더라도 일정한 내부 구조를 갖추고 있으면 자연어처리를 할 필요가 없다.
# - 문서간 유사성을 측정하는데 매우 적합
# - 문서에서 정확한 정보와 사실을 추출하는 일은 매우 어려움
# - 자연어 처리 알고리즘이 작동하는 이유를 설명하기 어려운 경우가 많음
# - 자연어 처리는 학습 데이터가 많이 필요함.

# # 16.2 언어와 통계
# ## 통계적 자연어 처리
# - 문제를 데이터와 숫자를 이용해 해결
# - 데이터셋과 연선 규모가 커지면서 통계적 자연어 처리에 기반한 방식이 두각.
# - 왜 작동하는지 설명하기가 어렵다.

# # 16.8 n-gram
# - 연속된 단어 (절)을 자연어 처리에서는 n-gram이라고 한다. 
# - bigram 을 단어로 취급하여 BoW특징값을 뽑고 단어 빈도와 문서 빈도 역수를 적용할 수 있다.
# - n-gram의 단점 : 학습에 필요한 데이터가 기하급수적으로 늘어남 

# In[11]:


import random, re
from collections import defaultdict, Counter
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt


# In[18]:


data = [ ("big data", 100, 15), ("Hadoop", 95, 25), ("Python", 75, 50),
         ("R", 50, 40), ("machine learning", 80, 20), ("statistics", 20, 60),
         ("data science", 60, 70), ("analytics", 90, 3),
         ("team player", 85, 85), ("dynamic", 2, 90), ("synergies", 70, 0),
         ("actionable insights", 40, 30), ("think out of the box", 45, 10),
         ("self-starter", 30, 50), ("customer focus", 65, 15),
         ("thought leadership", 35, 35)]

def text_size(total):
    return 8+total/200*20
for word, job_popularity, resume_popularity in data:
    plt.text(job_popularity, resume_popularity, word, ha='center', va='center',
            size=text_size(job_popularity+resume_popularity))

plt.xlabel("Popularity on the job Postings")
plt.ylabel("Popularity on Resumes")
plt.axis([0,100,0,100])
plt.xticks([])
plt.yticks([])
plt.show()


# In[56]:


def fix_unicode(text):
    return text.replace(u"\u2019", "'")

def get_document():

    url = "https://www.oreilly.com/radar/what-is-data-science/"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    content = soup.find("div", "article-body")         # find article-body div
    regex = r"[\w']+|[\.]"                             # matches a word or a period

    paragraph = []
    for paragraph in content("P"):
        words = re.findall(regex, fix_unicode(paragraph.text))
        document.extend(words)
    return document

transitions = defaultdict(list)
for prev, current in zip(document, document[1:]):
    transitions[prev].append(current)

def generate_using_bigrams() -> str:
    current = "."   # this means the next word will start a sentence
    result = []
    while True:
        next_word_candidates = transitions[current]    # bigrams (current, _)
        current = random.choice(next_word_candidates)  # choose one at random
        result.append(current)                         # append it to results
        if current == ".": return " ".join(result)     # if "." we're done
    


# In[59]:


generate_using_bigrams

