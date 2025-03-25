'''
SlidingPuzzleSolver

'''

'''
1
12 21
312 132 123 321 231 213
(...) 
12345678 (...) 87654321 <-- return only the leaves

'''
from node import No

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
Caso base + 2: lista com 3 números ; 4 espaços disponíveis para inserção ...



'''