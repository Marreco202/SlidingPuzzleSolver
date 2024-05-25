class No:
    id = -1
    vizinhos = []

    def __init__(self,id_in,vizinhos_in) -> None:
        self.id = id_in
        self.vizinhos = vizinhos_in
    
    def vizinho(self,no_de_estados):
        self.vizinhos.append(no_de_estados)