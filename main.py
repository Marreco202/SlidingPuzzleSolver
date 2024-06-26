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
from node import No

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
    # print("ainda nao troquei! ",lista)

    buf = lista[x_pos]
    lista[x_pos] = lista[new_x_pos]
    lista[new_x_pos] = buf
    # print("troquei! ",lista)
    return lista

def createGraph(combo_list):
    node_list = []

    for i in range(0,len(combo_list)):        
        buf = combo_list[i].copy()
        x_position = buf.index('x')
        inner_buff = [] #lista de vizinhos

        match x_position: #define quem são os vizinhos baseados na posição do x com um switch case
            case 8:
                possible_moves = (x_position-1,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
            case 7:
                possible_moves = (x_position+1,x_position-1,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[2]))
            case 6:
                possible_moves = (x_position+1,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
            case 5:
                possible_moves = (x_position+3,x_position-1,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[2]))
            case 4:
                possible_moves = (x_position+1,x_position-1,x_position+3,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[2]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[3]))
            case 3:
                possible_moves = (x_position+1,x_position+3,x_position-3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[2]))
            case 2:
                possible_moves = (x_position-1,x_position+3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
            case 1:
                possible_moves = (x_position-1,x_position+1,x_position+3)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[2]))
            case 0:
                possible_moves = (x_position+1,x_position+5)
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[0]))
                inner_buff.append(troca_x(buf.copy(),x_position,possible_moves[1]))
        node_list.append(No(i,inner_buff))
    return node_list

print("Calculando permutações...")
total_combo_list = permutation(1,9,list([]))
# print(total_combo_list)
grafo = createGraph(total_combo_list)

contador_de_arestas = 0

id_to_tuple = createHash(total_combo_list) # <int> id --> <lista> estado
tuple_to_id = invertDict(id_to_tuple) # <lista> estado --> <int> id

no_exemplo = 0
no_exemplo_naoTemAresta = -1

for no in grafo:
    # print(no.vizinhos) #RETIRAR COMENTARIO PARA VISUALIZAR A LISTA DE ADJACENCIAS
    for aresta in no.vizinhos:
        contador_de_arestas+=1
    if(list(id_to_tuple[no_exemplo]) not in no.vizinhos and no_exemplo_naoTemAresta == -1 and list(id_to_tuple[no.id]) != list(id_to_tuple[no_exemplo])): #caso nao esteja nos vizinhos e nao seja o proprio no... (impossivel haver lacos)
        no_exemplo_naoTemAresta = no.id

contador_de_arestas//=2 # cada no é contado de forma duplicada

'''
    TAREFA 1
'''
print("nos que nao tem aresta entre si (movimento invalido): ")
print("nó referência: ",list(id_to_tuple[no_exemplo]))
print("nó vizinho do nó referência: ", grafo[no_exemplo].vizinhos[0])
print("não vizinho do nó referência: ",list(id_to_tuple[no_exemplo_naoTemAresta]))


print("quantidade total de nos: ",len(total_combo_list))
print("quantidade total de arestas: ",contador_de_arestas)

'''
    TAREFA 2 e 3
'''


def bfs(G:list,s:No):
    visitados = [False] * len(G)
    fila = [(s,0)]

    total_camadas = 0
    componentes_conexas = 1

    jogo_inicial_maximo = []

    while fila: 
        no_buf = fila[0]
        camada = fila[0][1]
        id_buf = no_buf[0].id

        if(visitados[id_buf] == False): #adiciona os vizinhos do primeiro no da fila na lista
            for no in fila[0][0].vizinhos:
                fila.append((G[tuple_to_id[tuple(no)]],camada+1))
            visitados[id_buf] = True
            # print(camada)
        if(len(fila) == 1):
            total_camadas = camada
            # print(total_camadas)
        if(camada == 31 and componentes_conexas == 1):
            # print(list(id_to_tuple[fila[0][0].id]))
            jogo_inicial_maximo.append(list(id_to_tuple[fila[0][0].id]))

        fila.pop(0)
        if(not fila and False in visitados):
            # print("camadas da componente conexa {a}: {b}".format(a = componentes_conexas,b = camada))
            fila.append((G[visitados.index(False)],0))
            componentes_conexas+=1
    
    print("componentes_conexas: ",componentes_conexas)
    print("total camadas: ",total_camadas)
    return jogo_inicial_maximo

def print_matrix(lista):
    #parte do principio que toda lista tem tamanho 9 (matriz 3x3)
    i = 0
    while i<len(lista):
        print("|" , (lista[i]), (lista[i+1]), (lista[i+2]) , "|")
        i+=3
    return

max_movimentos = bfs(grafo,grafo[0])

print("Exemplo de configuração inicial que precisa de 31 movimentos até atingir a solução: ")
print_matrix(max_movimentos[0])
