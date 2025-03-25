'''
SlidingPuzzleSolver


1
12 21
312 132 123 321 231 213
(...) 
12345678 (...) 87654321 <-- return only the leaves

'''
from queue import SimpleQueue
from time import perf_counter

'''

Caso base: lista apenas com o numero 1 ;  2 espacos possiveis para inserção
Caso base + 1 : lista com 2 números ; 3 espaços disponíveis para inserção
Caso base + 2: lista com 3 números ; 4 espaços disponíveis para inserção

'''

def get_permutation_list(n:int):
    '''
    Recebe tamanho N do puzzle (e.g. 3 == 3x3 , 4 == 4x4 ...)
    
    Retorna lista de todas as folhas do grafo. Ou seja, todas as permutacoes destes n números

    '''

    n = n*n #Sempre será uma matriz quadrada
    permu_queue = SimpleQueue()
    permu_queue.put([1]) #TODO: CORRIGIR ISSO AQUI. POR CAUSA DISSO, EU TENHO QUE REMOVER OS 1's NO FINAL!


    while(True): #Enquanto todos os elementos da lista de permutacões forem menores do que 9, então continue permutando
        #O truque vai ser sempre colocar os elementos da permutacao atual no final da lista
        
        to_permute = permu_queue.get() #retira o elemento da fila
        tam = len(to_permute) #OBS: esse também é numero + 1 de inserções possíveis

        #sai do loop quando acabam as permutacoes
        if (tam > n): # Caso todos os elementos ja tenham sido permutados
            permu_queue.put(to_permute)
            break
        
        #realiza permutacoes com a iteracao atual
        else: #Caso contrario, ainda precisa inserir numeros distintos para a permutacao
            for i in range(0,tam):
                buf = to_permute.copy()
                buf.insert(i+1,tam+1) #exemplo: se a lista tem 2 elementos, entao esses são os elementos [1,2], logo tenho que inserir o 3 em 3 posicoes, 0 1 2
                permu_queue.put(buf)

    queue_size = permu_queue.qsize()
    print(queue_size)
    permu_list = []

    for i in range(0,queue_size):
        list_buf = permu_queue.get()
        list_buf.pop(0)
        permu_list.append(list_buf)


    return permu_list


t2_start = perf_counter()
lista = get_permutation_list(3)

t2_end = perf_counter()

r2 = t2_end - t2_start


print(f"get_permutation_list resultado: {t2_end-t2_start}")
print(len(lista))

# for el in lista:
#     print(el)

##TODO:
# 1- TESTAR COMBINACOES DE PERMUTACOES MELHOR --> SUSPEITA DE NAO ESTAR FAZENDO TODAS AS COMBINACOES

# 2- MONTAR O GRAFO A PARTIR DE CADA POSSIBILIDADE DE PERMUTACAO
# 3- DESCOBRIR COMPONENTES CONEXAS
# 4- CRIAR FUNCAO QUE, DADO ESTADO INICIAL, FAZ PASSO A PASSO DA SOLUCAO.
    # OU SEJA, PERCORRE O GRAFO!
    # OU SEJA, FAZ BUSCA DO ATUAL ATE O [2,3,4,5,6,7,8,9,10] P.E.
    #OU SEJA, TEMOS QUE ARBITRAR QUE O 10 EH O BURACO