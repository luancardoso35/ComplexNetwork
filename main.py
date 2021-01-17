import networkx as nx
import matplotlib.pyplot as plt

def triangles(graph):
    triangles = 0
    for node in graph:
        for neighbor in nx.neighbors(graph, node):
            for neighbor2 in nx.neighbors(graph, neighbor):
                for neighbor3 in nx.neighbors(graph, neighbor2):
                    if neighbor3.__eq__(node):
                        triangles = triangles + 1
    return triangles

def main():
    filePath = "C:\\Users\\Luan\\Downloads\\15email\\15email\\emailList.txt"

    graph = nx.read_adjlist(filePath, create_using=nx.DiGraph, nodetype=int)
    print("Número de nós = " + str(nx.number_of_nodes(graph)))
    print("Número de arestas = " + str(nx.number_of_edges(graph)))

    maxDegree = max([val for (node, val) in graph.out_degree()])
    minDegree = min([val for (node, val) in graph.out_degree()])

    media_out = sum([val for (node, val) in graph.out_degree()])/nx.number_of_nodes(graph)
    print("Grau médio de saída = ", media_out)
    media_in = sum([val for (node, val) in graph.in_degree()])/nx.number_of_nodes(graph)
    print("Grau médio de entrada = ", media_in)

    maxDegree1 = max([val for (node, val) in graph.in_degree()])
    minDegree1 = min([val for (node, val) in graph.in_degree()])

    print("Grau mínimo de saída = " + str(minDegree))
    print("Grau máximo de saída = " + str(maxDegree))
    print("Grau mínimo de entrada = " + str(minDegree1))
    print("Grau máximo de entrada = " + str(maxDegree1))
    print("Densidade da rede = " + str(nx.density(graph)))

    print("Número de triângulos no grafo (self loops) = " + str(triangles(graph)))

    print("Média do clustering (coeficiente de agrupamento) = " + str(nx.average_clustering(graph)))

    print("Na tentativa de encontrar o Diâmetro, usando o máximo das excentricidades ou o próprio"
          "método que retornava o diâmetro do grafo,\no seguinte erro foi encontrado: "
          "networkx.exception.NetworkXError: Found infinite path length because the graph is not connected")


    print("Número de componentes conexos = " + str(nx.number_strongly_connected_components(graph)))

    print("\nBuscando os nós mais importantes: \n1) Através da centralidade do autovetor")
    dict = nx.eigenvector_centrality(graph)
    listofTuples = sorted(dict.items() , reverse=True, key=lambda x: x[1])
    print("Três nós mais importantes segundo a centralidade do autovetor "
          "(primeiro item da tupla indica o nó, e o segundo indica a centralidade do mesmo):")
    print((listofTuples[0]))
    print((listofTuples[1]))
    print((listofTuples[2]))

    print("\n2) Pelo maior grau de entrada:")
    dict = sorted(graph.in_degree, key=lambda x: x[1], reverse=True)
    print("Três nós mais importantes segundo o grau de entrada (o primeiro item indica o nó e o segundo seu grau:")
    print(dict[0])
    print(dict[1])
    print(dict[2])

    print("\n3) Pelo maior grau de saída:")
    dict = sorted(graph.out_degree, key=lambda x: x[1], reverse=True)
    print("Três nós mais importantes segundo o grau de saída (o primeiro item indica o nó e o segundo seu grau:")
    print(dict[0])
    print(dict[1])
    print(dict[2])



    # No caso da betweenness centrality, Foi tentado encontrar o nó com maior betweenness
    # centrality, porém o cálculo leva muito tempo a ser feito, fazendo com que o programa
    # tivesse que ficar semanas ou até meses rodando para encontrar um valor. O código abaixo
    # mostraria os três nós mais importantes segundo esse quesito:

    # print("\n4) Através de betweenness centrality:")
    # dict1 = nx.betweenness_centrality(graph, k=graph.number_of_nodes())
    # listofTuples = sorted(dict1.items() , reverse=True, key=lambda x: x[1])
    # print("Três nós mais importantes segundo a centralidade do autovetor "
    #      "(primeiro item da tupla indica o nó, e o segundo indica a centralidade do mesmo):")
    # print((listofTuples[0]))
    # print((listofTuples[1]))
    # print((listofTuples[2]))




if __name__ == "__main__":
    main()




