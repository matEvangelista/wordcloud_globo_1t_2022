from cgi import print_form
from re import T
from shutil import ExecError
from bs4 import BeautifulSoup
import requests as re

url = 'https://www.poder360.com.br/eleicoes/leia-a-transcricao-do-debate-presidencial-da-globo/'
page = re.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

# no site, todos os candidatos e Bonner seguem a seguinte estrutura:
"""
    <p> <strong>Nome</strong> p1</p>
    <p> p2 </p>
    ...
"""
# então, basta procurar cada <p> e, dentro de cada um, encontrar cada <strong>
# se não houver strong, será considerado como parágrafo do mesmo autor, por exemplo:
# <strong>William Bonner</strong>
# None
# None
# None
# ou seja, há 4 parágrafos ditos por ele

pessoas = ['Ciro', "Felipe", 'Jair', 'Luiz',
           'Padre', 'Simone', 'Soraya', 'William']


def retorna_falas_por_pessoa(nome, soup):
    comeco = 5 if nome == 'Luiz' else 2
    paragrafos = soup.find_all('p')
    falas = []
    j = 0
    for i in range(len(paragrafos)):
        try:
            if (nome in paragrafos[i].find('strong').text):
                falas.append(' '.join(paragrafos[i].text.split()[comeco:]))
                for j in range(i + 1, len(paragrafos)):
                    if (paragrafos[j].find('strong') == None):
                        falas.append(paragrafos[j].text)
                    else:
                        break
        except:
            pass
    return falas

for pessoa in pessoas:
    with open ('textos/{0}.txt'.format(pessoa), 'w', encoding='utf-8') as arq:
        arq.write('\n'.join(retorna_falas_por_pessoa(pessoa, soup)))

