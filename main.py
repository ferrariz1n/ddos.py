import requests
import time

tabela=[]
url = input(str('Digite qualquer coisa: '))
for i in range(10):
  tabela.append(requests.get(url))
  time.sleep(0.01)

while True:
  print(tabela)
  time.sleep(0.01)
