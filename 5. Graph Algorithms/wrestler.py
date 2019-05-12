from collections import defaultdict
import graph as g

def PrintColor(color):
    if not color:
        print('Not possible\n')
    else:
        group = defaultdict(list)
        for v, c in color.items():
            if c == 1:
                group['Babyfaces'].append(v)
            else:
                group['Heels'].append(v)
        print('Yes possible')
        for c, v in group.items():
            print('{0}: {1}'.format(c, ' '.join(v)))
        print()

def readfile(file):
    with open(file) as f:
        V = int(next(f))
        graph = g.Graph(V)
        for _ in range(V):
            next(f)
        E = int(next(f))
        for _ in range(E):
            args = [x for x in next(f).split()]
            graph.AddEdge(args[0], args[1])
    return graph

def solve(file):
    graph = readfile(file)
    color = graph.Bipartite()
    print(file)
    PrintColor(color)

if __name__ == '__main__':
    solve('wrestler1.txt')
    solve('wrestler2.txt')
    solve('wrestler.txt')