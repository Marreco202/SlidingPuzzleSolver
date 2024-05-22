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
from node import Node

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

def createHash(combo_list): # id : combo
    dicio = {}
    for i in range(0,len(combo_list)):
        dicio[i] = tuple(combo_list[i])
    return dicio

def invertDict(dicio): # combo : id
    # print("Hello there!")
    return dict((v, k) for k, v in dicio.items())

def troca_x(lista,x_pos,new_x_pos):
    buf = lista[x_pos]
    lista[x_pos] = lista[new_x_pos]
    lista[new_x_pos] = buf
    return lista

def createGraph(combo_list,id_to_tuple,tuple_to_id):
    node_list = []

    for i in range(0,len(combo_list)):        
        buf = combo_list[i]
        x_position = buf.index('x')
        inner_buff = [] #lista de vizinhos

        match x_position: #define quem são os vizinhos baseados na posição do x com um switch case
            case 8:
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 7:
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 6:
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 5:
                inner_buff.append(troca_x(buf,x_position,x_position+3))
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 4:
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position+3))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 3:
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position+3))
                inner_buff.append(troca_x(buf,x_position,x_position-3))
            case 2:
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position+3))
            case 1:
                inner_buff.append(troca_x(buf,x_position,x_position-1))
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position+3))
            case 0:
                inner_buff.append(troca_x(buf,x_position,x_position+1))
                inner_buff.append(troca_x(buf,x_position,x_position+5))

        node_list.append(Node(i,inner_buff)) #nao sei se funciona, deve funcionar.
    return node_list

print("Calculando permutações...")
total_combo_list = permutation(1,9,list([]))
# print(total_combo_list)
print("tamanho da lista: ",len(total_combo_list))

