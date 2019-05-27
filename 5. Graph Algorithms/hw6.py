import graph as g

def PrintDist(dist, src):
    print('Dijkstra\'s algorithm')
    print('Source: {0}'.format(src))
    print('Vertex\tDistance')
    for v, d in dist.items():
        print('{0}\t{1}'.format(v, d))
    print()

if __name__ == '__main__':
    graph = g.Graph()
    graph.AddDirected('A','B',8)
    graph.AddDirected('A','F',10)
    graph.AddDirected('F','A',5)
    graph.AddDirected('H','A',4)
    graph.AddDirected('F','B',7)
    graph.AddDirected('H','B',9)
    graph.AddDirected('F','C',3)
    graph.AddDirected('G','H',3)
    graph.AddDirected('B','C',4)
    graph.AddDirected('C','D',3)
    graph.AddDirected('D','F',18)
    graph.AddDirected('B','E',10)
    graph.AddDirected('E','G',7)
    graph.AddDirected('G','D',2)
    graph.AddDirected('E','D',9)
    graph.AddDirected('D','E',25)
    graph.AddDirected('F','E',2)
    dist = graph.Dijkstra('G')
    PrintDist(dist, 'G')
