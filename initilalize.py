import os

if os.path.exists('/urls') != True:
  os.system('mkdir urls')
  
if os.path.exists('/urls/urls.csv') != True:
  fp.open('urls.csv', 'w+')
