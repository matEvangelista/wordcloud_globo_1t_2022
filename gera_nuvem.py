from turtle import width
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import sys, os
import nltk
import wordcloud
os.chdir(sys.path[0])

nome_arquivo = []
candidatos = ['Ciro', 'Felipe', 'Jair', 'Luiz', 'Padre', 'Simone', 'Soraya', 'William']
continuar = True
while(continuar):
    active = True
    while(active):
        print("\nOpções: \n\tCiro\n\tFelipe\n\tJair\n\tLuiz\n\tPadre\n\tSimone\n\tSoraya\n\tWilliam")
        candidato = input("Digite o nome do candidato: ").title()
        if candidato in candidatos:
            active = False
        else:
            print("Nome inválido, por favor digite novamente.\n")

    active = True
    while(active):
        arquivo = input("Digite o nome do arquivo a ser salvo: ")
        
        if arquivo not in nome_arquivo:
            if arquivo != ' ':
                nome_arquivo.append(arquivo)
                active = False    
        else:
            print("Voce ja criou um arquivo com esse nome.\n")

    # text = open(f'{candidato}.txt', mode='r', encoding='utf-8').read()
    text=open('textos/'+f'{candidato}.txt',mode='r',encoding='utf-8').read()

    nltk.download('stopwords')
    stopwords = nltk.corpus.stopwords.words('portuguese')

    wc = WordCloud(
        background_color = 'white',
        stopwords = stopwords,
        width = 400,
        height=600
    )

    wc.generate(text)

    wc.to_file('salvos/'+f'{arquivo}.png')
    print("Nuvem de palavras gerada, cheque a pasta para vizualizar a imagem.\n")

    active = True
    while(active):
        again = input("Continuar? s/n ")
        if again == 's':
            active = False
        elif again == 'n':
            active = False
            continuar = False
        else:
            print('Resposta invalida, tente novamente.\n')


