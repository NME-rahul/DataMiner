import pandas as pd

def take_input():
  df = pd.read_csv('/urls/urls.csv')
  print("write 'end' for end of urls\n")
  while(True):
    url = input()
    if url == 'end':
      break
      
