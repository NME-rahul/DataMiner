import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

Error0 = 'Error: in internet connection.'


def control_tag(word, tag, soup):
  with open('data.txt', 'w') as fp:
    sentence = ''; start = 0; end = 0;
    for i in soup.findAll(tag):
      sentence = i.text
      print(type(sentence))
      fp.write(sentence)
      if word in sentence:
        print(word)

def collect_data(keywords):
  df = pd.read_csv('urls/urls.csv')
  
  for i in range(len(df)):
    try:
      res = rq.get(df['urls'][i])
    except:
      print(Error0)
    soup = BeautifulSoup(res.content, 'html.parser')
    
    #based on class
    #based on keyword
    tags = ['title', 'h1', 'h2', 'h3', 'p']
    
    for word in keywords:
      for tag in tags:
        print(word, tag)
        control_tag(word, tag, soup)
