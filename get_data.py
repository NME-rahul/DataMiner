import pandas as pd
import requests as rq
from bs4 import BeautifulSoup

Error0 = 'Error: in internet connection.'

def collect_data(keywords):
  df = pd.read_csv('/data/urls.csv')
  
  for i in range(len(df)):
    try:
      res = rq.get(df['url'][i])
    except:
      print(Error0)
    soup = BeautifulSoup(res.content, 'html.parser')
    #based on class
    #based text keywords
    text = []
    start = 0; end = 0;
    fp = open('data.txt', 'w')
    for word in keywords:
      fp.write(word + '\n')
      for i in soup.findAll('p'):
        text.append(i)
        if word in text or (start == 0 or start > 0):
          fp.write(i)
          start = start + 1
          #write in data file, write next 50 word and until '.'
        if start == 50:
          start = 0
          break
      text.clear()
      for i in soup.findAll('h1'):
        text.append(i)
        if word in text or (start == 0 or start > 0):
          fp.write(i)
          start = start + 1
          #write in data file, write next 50 word and until '.'
        if start == 50:
          start = 0
          break
          #write in data file
      text.clear()
      for i in soup.findAll('h2'):
        text.append(i)
        if word in text or (start == 0 or start > 0):
          fp.write(i)
          start = start + 1
          #write in data file, write next 50 word and until '.'
        if start == 50:
          start = 0
          break
          #write in data file
      text.clear()
      for i in soup.findAll('h3'):
        text.append(i)
        if word in text or (start == 0 or start > 0):
          fp.write(i)
          start = start + 1
          #write in data file, write next 50 word and until '.'
        if start == 50:
          start = 0
          break
          #write in data file
      text.clear()
