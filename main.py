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

# for i in range(0,10):
#     q.put(i)

# for i in range(0,10):
#     print(q.get())

#metodos get e put  

total_combo_list = []

#Funcao antiga

def permutation(ini,n,combo):
    if(ini == n):
        qg = []
        for i in range(0,n):
            combo.insert(i,'x')
            total_combo_list.append(combo)
            buf = combo.copy()
            qg.append(buf)
            combo.remove('x')
        return qg

    permu_list = []
    for i in range(0,ini):
        combo.insert(i,ini)
        r = permutation(ini+1,n,combo)
        for el in r:
            permu_list.append(el)
        combo.remove(ini)
    return permu_list



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

    lista_tam = n*n #Sempre será uma matriz quadrada
    permu_queue = SimpleQueue()
    permu_queue.put([1])


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
                buf.insert(i,i+1) #exemplo: se a lista tem 2 elementos, entao esses são os elementos [1,2], logo tenho que inserir o 3 em 3 posicoes, 0 1 2
                permu_queue.put(buf)


    print(permu_queue.qsize())

    return

t1_start = perf_counter()
permutation(1,9,list([]))
t1_end = perf_counter()

r1 = t1_end - t1_start

t2_start = perf_counter()
get_permutation_list(3)
t2_end = perf_counter()

r2 = t2_end - t2_start


print(f"permutation resultado: {t1_end-t1_start}")
print(f"get_permutation_list resultado: {t2_end-t2_start}")

print(f"r2/r1 : {r2/r1}%")