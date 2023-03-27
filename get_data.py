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
    for i in soup.findAll('p'):
      text.append(i)
      if 'one of them keyword in text' in text:
        #write in data file, write next 50 word and until '.'
    for i in soup.findAll('h1'):
      text.append(i)
      if 'one of them keyword in text' in text:
        #write in data file
    for i in soup.findAll('h2'):
      text.append(i)
      if 'one of them keyword in text' in text:
        #write in data file
    for i in soup.findAll('h3'):
      text.append(i)
      if 'one of them keyword in text' in text:
        #write in data file
