'''
SlidingPuzzleSolver


1
12 21
312 132 123 321 231 213
(...) 
12345678 (...) 87654321 <-- return only the leaves

'''
from queue import SimpleQueue
from time import perf_counter, sleep
import networkx as nx
import matplotlib.pyplot as plt

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
                buf.insert(i+1,tam) #exemplo: se a lista tem 2 elementos, entao esses são os elementos [1,2], logo tenho que inserir o 3 em 3 posicoes, 0 1 2
                permu_queue.put(buf)

    queue_size = permu_queue.qsize()
    # print(queue_size)
    permu_list = []

    for i in range(0,queue_size):
        list_buf = permu_queue.get()
        list_buf.pop(0)
        permu_list.append(list_buf)


    return permu_list

def create_adj_dict(permu_list: list) -> dict:

    dicio_adj = {}


    for current_state in lista:
        where_is_x = current_state.index(9) # O numero 9 representa o espaço vazio 'x' do quebra-cabeça 3x3
        vizinhos = [where_is_x - 1, where_is_x + 1,where_is_x - 3, where_is_x + 3] #assume que todo tile tem 4 adjacencias | esquerda, direita, cima, baixo

        if(where_is_x % 3 == 0): # ou seja, coluna da esquerda...
            vizinhos.remove(where_is_x-1)
        elif(where_is_x%3 == 2): # ou seja, coluna da direita...
            vizinhos.remove(where_is_x+1)

        for v in vizinhos:
            if v < 0 or v >= 9:
                vizinhos.remove(v) #remove todos os vizinhos que são posicoes invalidas

        new_value = []
        
        # vizinhos:
            # 1 2 3
            # 4 5 6
            # 7 8 9


        for v in vizinhos: # vizinhos: lista de indices na matriz de quem sao seus vizinhos
            # print("======")
            buf_state = current_state.copy() # estado buffer para nao ferrar com a referncia para outras chamadas
            # print('estado atual: ',buf_state)
            to_trade = current_state[v] # valor adjacente a ser trocado. v é o indice dele no estado atual
            # print('quem eu quero trocar de lugar: ',to_trade)
            buf_state.remove(9) # remove o 'x'
            buf_state.insert(v,9) # move o 'x' para a posicao do adjacente
            buf_state.remove(to_trade) # remove o valor do vizinho adjacente ao buraco antigo
            buf_state.insert(where_is_x,to_trade) # insere ele na antiga posicao do 'x'
            new_value.append(tuple(buf_state)) # adiciona nova tupla como sendo valor valido a partir do current_state
            # print("estado final: ",buf_state)
            # print("======")
        
        dicio_adj[tuple(current_state)] = new_value # adiciona no dicionario lista de tuplas vizinhas


    return dicio_adj

if __name__  == "__main__":

    t2_start = perf_counter()

    lista = get_permutation_list(3)
    t2_end = perf_counter()

    r2 = t2_end - t2_start

    # Cria estados

    print(f"1. get_permutation_list resultado: {t2_end-t2_start}")

    adj_dict = create_adj_dict(lista)

    # Cria estados

    print(f"2. dicio_adj resultado: {perf_counter() - t2_start}")

    G = nx.Graph()

    tam = len(lista)

    i = 0

    for key in adj_dict:
        G.add_node((i, tuple(adj_dict[key])))
        i+=1

    # print(G)

    nx.draw(G)
    plt.show()

##TODO:
# 1- TESTAR COMBINACOES DE PERMUTACOES MELHOR --> SUSPEITA DE NAO ESTAR FAZENDO TODAS AS COMBINACOES (CHECK)

# 2- MONTAR O GRAFO A PARTIR DE CADA POSSIBILIDADE DE PERMUTACAO (CHECK)

# 3- DESCOBRIR COMPONENTES CONEXAS
# 4- CRIAR FUNCAO QUE, DADO ESTADO INICIAL, FAZ PASSO A PASSO DA SOLUCAO.
    # OU SEJA, PERCORRE O GRAFO!
    # OU SEJA, FAZ BUSCA DO ATUAL ATE O [2,3,4,5,6,7,8,9,10] P.E.
    #OU SEJA, TEMOS QUE ARBITRAR QUE O 10 EH O BURACO