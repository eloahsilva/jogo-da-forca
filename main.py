import os
import random

forca = ['''
  +---+
  |   |
  |   O
  |  /|\  
  |  / \ 
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|\  
  |  /  
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|\  
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |  /|  
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   O
  |    
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   |
  |   
  |    
  |    
  | 
  +=========   
  ''',
  '''
  +---+
  |   
  |   
  |    
  |    
  | 
  +=========   
  ''']


def escolhe_palavra(tema):
  temas = ['Animais', 'Comidas', 'Profissões']
  arquivo = open(f'{temas[tema - 1]}.txt', 'r')
  palavra = random.choice(arquivo.readlines()).strip()
  arquivo.close()
  return (palavra, temas[tema - 1])

def menu():
    os.system('cls')
    print ('-' * 30)
    print ('  J O G O   D A   F O R C A')
    print ('-' * 30)
    print ('Animais = 1')
    print ('Comidas = 2')
    print ('Profissões = 3')
    print ('Sair = 0')
    print (' ')

def jogo():
    palavra, nome_arquivo = escolhe_palavra(int(tema))
    os.system('cls')

    tentativas = 7
    palpites = []
    while tentativas:
        os.system('cls')
        print ('Tema escolhido: {} \n'.format(nome_arquivo))
        print(forca[tentativas - 1])

        for letra in palavra:
            if letra == ' ':
                print (letra, end= '')
            elif letra in palpites and letra in palavra:
                print (letra, end='')
            else:
                print (' _ ', end= '')
        print ('\n\nVocê tem {} tentativas.\n\n'.format(tentativas))
        print('Palpites: {}'.format(palpites))
        #print(palavra)
        palpite = input('Adivinhe uma letra ou a palavra: ')
        palpites.append(palpite.upper().strip())
        if palpite.upper().strip() not in palavra:
            tentativas -= 1
    
        if palavra in palpites:
            os.system('cls')
            print('Parabéns! Você venceu')
            print('A palavra era {} \n'.format(palavra))
            tentativas = 0
            break

        elif tentativas == 0:
            os.system('cls')
            print('Você foi enforcado')
            print('A palavra era {} \n'.format(palavra))


tema = ''
while(tema not in ['1', '2', '3']):
    menu()
    tema = input('Escolha um tema e digite o número correspondente: ')
    if tema == '0':
        break
    else:
        jogo()
        tema = ''
        input('Pressione Enter para continuar')