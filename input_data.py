def get_urls():
  fp = open('/data/urls.csv', 'r+')
  print("write 'end' for end of urls\n")
  while(True):
    url = input()
    if url == 'end':
      break
    fp.write(url+',\n')
  
  fp.close()
   
def get_keywords():
  keywords = []
  print("write '.end' for end of keywords\n")
  while(True):
    keywords.append(input())
    if keywords[len(keywords) - 1] == '.end':
      break
      
  return keywords
