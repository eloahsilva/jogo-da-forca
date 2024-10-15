import random

def escolhe_palavra(tema:int):
  temas = ['animais', 'comidas', 'profissoes']
  arquivo = open(f'{temas[tema - 1]}.txt', 'r')
  palavra = random.choice(arquivo.readlines()).strip()
  arquivo.close()
  return (palavra, temas[tema - 1])

teste = escolhe_palavra(2)
print(teste)