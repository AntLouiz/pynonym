import requests
from bs4 import BeautifulSoup


url = 'https://www.sinonimos.com.br/desenvolver/'
response = requests.get(url)

if response.status_code != 200:
    print("Houve um problema na requisição")

content = response.text
parser = BeautifulSoup(content, 'html.parser')

all_sym = parser.findAll('a', {'class' : 'sinonimo'})
print(all_sym)
