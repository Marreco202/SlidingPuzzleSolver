'''
Trabalho 2 - Análise de Algoritmos

Alunos:
    Guilherme Ponce - 2011179
    João Victor Godinho - 2011401
'''

'''
1
12 21
312 132 123 321 231 213
(...) 
12345678 (...) 87654321 <-- retornar apenas as folhas

1) retornar as folhas
2) dar append na lista de x em todas as posições entre eles
    --> .insert(indicie) até indice len(n-1)

'''

total_combo_list = []

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


print("Calculando permutações...")
total_combo_list = permutation(1,9,list([]))
print(total_combo_list)
print("tamanho da lista: ",len(total_combo_list))

# f = open("out.txt","w")
# f.write(str(total_combo_list))
