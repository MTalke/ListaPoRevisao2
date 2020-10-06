# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from collections import defaultdict



if __name__ == "__main__":
    
    class Grafo(object):
        """ Implementacaoo basica de um grafo. """

        def __init__(self, arestas, direcionado=False):
            """Inicializa as estruturas base do grafo."""
            self.adj = defaultdict(set)
            self.direcionado = direcionado
            self.adiciona_arestas(arestas)


        def get_vertices(self):
            """ Retorna a lista de vertices do grafo. """
            return list(self.adj.keys())
        
        def vertices_vetor(self):
            """ Retorna a lista de vertices do grafo. """
            return list(self.adj.keys())

        def get_arestas(self):
            """ Retorna a lista de arestas do grafo. """
            return [(k, v) for k in self.adj.keys() for v in self.adj[k]]


        def adiciona_arestas(self, arestas):
            """ Adiciona arestas ao grafo. """
            for u, v in arestas:
                self.adiciona_arco(u, v)


        def adiciona_arco(self, u, v):
            """ Adiciona uma ligacao (arco) entre os nodos 'u' e 'v'. """
            self.adj[u].add(v)
            if not self.direcionado:
                self.adj[v].add(u)


        def existe_aresta(self, u, v):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return u in self.adj and v in self.adj[u]

        def grau(self, u):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return len(self.adj[u])
        
        def verticesAdjacentes(self, u):
            """ Existe uma aresta entre os vertices 'u' e 'v'? """
            return self.adj[u]

        def __len__(self):
            return len(self.adj)


        def __str__(self):
            return '{}({})'.format(self.__class__.__name__, dict(self.adj))


        def __getitem__(self, v):
            return self.adj[v]
    

    def leituraArquivo():
        arq = open('arquivo1.txt', 'r')  #abre o arquivo
        texto = []  #declaro um vetor
        arestas = [] #declaro um segundo vetor
        matriz2 = [] #declaro um terceiro vetor
        texto = arq.readlines() #quebra as linhas do arquivo em vetores 

        for i in range(len(texto)):        
            arestas.append(texto[i].split())
            
        arq.close()

        return arestas
    
    def Menu():
        print("Escolha a opcao que deseja")
        print("Escolha 6 para questao 6")
        print("Escolha 7 para questao 7")
        print("Escolha 8 para questao 8")
        print("Escolha 9 para questao 9")
        print("Escolha 10 para questao 10")
        opcao = int(input("digite a opcao: "))

        if (opcao == 6):
            questao6()
        elif(opcao == 7):
            questao7()
        elif(opcao == 8 ):
            questao8()
        elif(opcao == 9):
            questao9()
        elif(opcao == 10):
            questao10()
        else:
            print("Nao tem essa questao")
            Menu()

    def questao6():
        arestas = leituraArquivo()
        print("Grafo arestas", arestas)
        vertices = []
        grafo = Grafo(arestas, direcionado=False)
        print(grafo.adj)
        print("vertices:", grafo.get_vertices())
        print("numero de vertices:", len(grafo.get_vertices()))
        x = 1
        while x <= 6:
            opcao = int(input("digite o vertice para saber qual e o grau dele: "))
            print(grafo.grau(str(opcao)))
            x = x + 1
    
    def questao7():
        arestas = leituraArquivo()
        grafo = Grafo(arestas, direcionado=False)
        print(grafo.adj)
        print("vertices:", grafo.get_vertices())
        print("numero de vertices:", len(grafo.get_vertices()))
        x = 1
        while x <= 6:
            opcao = int(input("digite o vertice para saber qual e o seu(s) vertices adjacentes "))
            print(grafo.verticesAdjacentes(str(opcao)))
            x = x + 1
            
    def questao8():
        vetor = [2,4,5]
        print("Elementos do vetor", vetor)
        resultado = soma_vetor(vetor)
        print("total:", resultado)
        
    def soma_vetor(vetor):
        if len(vetor) == 1:
            return vetor[0]
        else:
            return vetor[0] + soma_vetor(vetor[1:])
        
        
    def questao9():
        numero = int(input("digite um numero maior que zero: "))
        if (numero > 0):
            resultado= 0
            i = 1
            while i  <= numero:  
                resultado = i*(i+1) + resultado
                i = i + 1;

            print("Resultado", resultado)

    def questao10():
        arq = open('arquivo2.txt', 'r')  #abre o arquivo
        texto = []  #declaro um vetor
        matriz1 = [] #declaro um segundo vetor
        matriz2 = [] #declaro um terceiro vetor
        texto = arq.readlines() #quebra as linhas do arquivo em vetores 
        
        for i in range(len(texto)):        
            if(i < 10):
                matriz1.append(texto[i].split())
            else:
                if(texto[i] != '\n'):
                    matriz2.append(texto[i].split())
        resultado = 0
        multiplicando = multiplicaMatrizes(matriz1,matriz2)
        print("Resultado do somatorio das matrizes", multiplicando)
        arq.close()

    def multiplicaMatrizes(matriz, matriz2):
        if(len(matriz) != len(matriz2) or len(matriz[0]) != len(matriz2[0])):
            return None
        result = []
        multiplica = 0
        for i in range(len(matriz)):   
            result.append([])
            for j in range(len(matriz[0])):
                multiplica = int(matriz[i][j]) * int(matriz2[i][j]) + multiplica
        return multiplica
    
Menu()