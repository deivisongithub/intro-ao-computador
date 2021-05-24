#Aluno: Deivison rodrigues jordao
#Busca binaria

#Definindo funcoes

def binary_search(vetor,elemento, begin=0, end=None):
    if end is None:
        end = len(vetor)-1
    if begin <= end:
        m = (begin + end)//2
        if vetor[m] == elemento:
            return True
        if elemento < vetor[m]:
            return binary_search(vetor,elemento, begin, m-1)
        else:
            return binary_search(vetor,elemento, m+1, end)
    return False


#Producao do vetor

from random import randint

tamanho = int(input("digite a quantidade de elementos(e o intevalo numero que sera gerado) que o vetor tera: "))

vetor_de_numeros = [randint(0,tamanho) for i in range(tamanho)]
vetor_de_numeros.sort()

#Processamento

elemento_bucado = int(input("digite o elemento que deseja buscar: "))

#Saida
print(binary_search(vetor_de_numeros,elemento_bucado))
  