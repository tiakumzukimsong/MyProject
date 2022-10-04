import requests
from bs4 import BeautifulSoup




a = requests.get(input(print("Enter the link : ")))


soup = BeautifulSoup(a.content, 'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))
