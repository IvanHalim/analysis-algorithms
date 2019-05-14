from collections import defaultdict, deque

class Heap:
    def __init__(self):
        self.array = []
        self.pos   = {}
        self.size  = 0

    def NewMinHeapNode(self, v, dist):
        return [v, dist]
        
    # A utility function to swap two nodes
    def SwapMinHeapNode(self, a, b):
        t = self.array[a]
        self.array[a] = self.array[b]
        self.array[b] = t

    # This is the heapify down function of a minimizing heap
    def HeapifyDown(self, parent_idx):

        # First we assume that the parent node is the smallest
        smallest    = parent_idx
        left_child  = 2 * parent_idx + 1
        right_child = 2 * parent_idx + 2

        # Next we're going to check if the child nodes are larger than the parent node
        if left_child < self.size and self.array[left_child][1] < self.array[smallest][1]:
            smallest = left_child
        if right_child < self.size and self.array[right_child][1] < self.array[smallest][1]:
            smallest = right_child

        # If the parent node is not the smallest node
        # We swap the value of the parent node with the smallest node
        # We repeat this process until we reach the bottom of the heap
        if smallest != parent_idx:
            # Update the position of the nodes
            self.pos[self.array[smallest][0]]   = parent_idx
            self.pos[self.array[parent_idx][0]] = smallest

            # Swap nodes
            self.SwapMinHeapNode(smallest, parent_idx)
            self.HeapifyDown(smallest)

    # Function to extract the minimum node from heap
    # which is the root node of a minimizing heap
    def ExtractMin(self):
        # Return NULL if heap is empty
        if self.IsEmpty():
            return

        # Store the root node
        root = self.array[0]

        # Replace root node with last node
        last_node = self.array[self.size - 1]
        self.array[0] = last_node

        # Update the position of the nodes
        self.pos[last_node[0]] = 0
        self.pos[root[0]] = self.size - 1

        # Reduce heap size and heapify root
        self.size -= 1
        self.HeapifyDown(0)

        return root

    def IsEmpty(self):
        return True if self.size == 0 else False

    def DecreaseKey(self, v, dist):
        # Get the index of v in heap array
        idx = self.pos[v]

        # Get the node and update its dist value
        self.array[idx][1] = dist

        # Heapify up while this node is smaller than its parent
        while idx > 0 and self.array[idx][1] < self.array[int((idx - 1) / 2)][1]:
            # Swap thid node with its parent
            self.pos[self.array[idx][0]] = int((idx - 1) / 2)
            self.pos[self.array[int((idx - 1) / 2)][0]] = idx
            self.SwapMinHeapNode(idx, int((idx - 1) / 2))

            # Move to parent index
            idx = int((idx - 1) / 2)

    def IsInMinHeap(self, v):
        if self.pos[v] < self.size:
            return True
        return False

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    # Adds an edge to an undirected graph
    def AddEdge(self, src, dest, weight=1):
        # Add an edge from src to dest. A new node
        # is added to the adjacency list of src.
        self.graph[src].append([dest, weight])

        # Since graph is undirected, add an edge
        # from dest to src also
        self.graph[dest].append([src, weight])

    # Adds an edge to a directed graph
    def AddDirected(self, src, dest, weight=1):
        # Add an edge from src to dest. A new node
        # is added to the adjacency list of src.
        self.graph[src].append([dest, weight])

    # The main function that calculates distances
    # of shortest paths from src to all vertices.
    # It is a O(ELogV) function
    def Dijkstra(self, src):
        dist = {}       # Array to store distance of vertices from source
        heap = Heap()   # Heap to store unselected vertices

        # Initialize min heap with all vertices
        # and distance array as all infinity
        i = 0
        for v in self.graph.keys():
            dist[v] = float('inf')
            heap.array.append(heap.NewMinHeapNode(v, dist[v]))
            heap.pos[v] = i
            i += 1

        # Set the dist value of src node to 0
        dist[src] = 0
        heap.DecreaseKey(src, dist[src])

        # Initialize size of min heap to V, the number
        # of vertices in the graph
        heap.size = self.V

        # The loop continues until all the vertices
        # have been finalized
        while not heap.IsEmpty():
            # Extract the vertex with minimum distance value
            u = heap.ExtractMin()[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # distance values
            for neighbor in self.graph[u]:
                v = neighbor[0]

                # If shortest distance to v is not finalized
                # yet, and distance to v through u is less
                # than its previously calculated distance
                if heap.IsInMinHeap(v) and neighbor[1] + dist[u] < dist[v]:
                    dist[v] = neighbor[1] + dist[u]
                    heap.DecreaseKey(v, dist[v])

        return dist

    def OptimalLoc(self):
        max_dist, optimal_loc = min((max(self.Dijkstra(v).values()), v) for v in self.graph.keys())
        return max_dist, optimal_loc

    # The main function that prints the Minimum  
    # Spanning Tree(MST) using the Prim's Algorithm.  
    # It is a O(ELogV) function 
    def PrimMST(self, src):
        key    = {}      # To store the distances of vertices to their nearest neighbors
        parent = {}      # To store the parents of vertices
        heap   = Heap()  # Heap to store unselected vertices

        # Initialize min heap with all vertices
        # key as all infinity
        # parent as all -1 (no parent)
        i = 0
        for v in self.graph.keys():
            parent[v] = -1
            key[v] = float('inf')
            heap.array.append(heap.NewMinHeapNode(v, key[v]))
            heap.pos[v] = i
            i += 1

        # Set the key value of src node to 0
        key[src] = 0
        heap.DecreaseKey(src, key[src])

        # Initialize size of min heap to V, the number
        # of vertices in the graph
        heap.size = self.V

        # The loop continues until all the vertices
        # have been finalized
        while not heap.IsEmpty():
            # Extract the vertex with minimum key value
            u = heap.ExtractMin()[0]

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # key values
            for neighbor in self.graph[u]:
                v = neighbor[0]

                # If distance to v is not finalized yet,
                # and distance to v is less than its
                # previously calculated distance
                if heap.IsInMinHeap(v) and neighbor[1] < key[v]:
                    key[v] = neighbor[1]
                    parent[v] = u
                    heap.DecreaseKey(v, key[v])

        return parent

    def BipartiteUtil(self, color, src):
        # Assign first color to source
        color[src] = 1

        # Create a queue (FIFO) of vertices and enqueue
        # source vertex for BFS traversal
        queue = deque()
        queue.append(src)

        # Run while queue is not empty
        while queue:
            u = queue.popleft()

            # Return false if there is a self-loop
            if u in self.graph[u]:
                return False

            # Traverse through all adjacent vertices of
            # u (the extracted vertex) and update their
            # color assignment
            for neighbor in self.graph[u]:
                v = neighbor[0]

                # If vertex v has not been visited yet
                if color[v] == -1:
                    # Assign alternate color to v
                    color[v] = 1 - color[u]
                    queue.append(v)

                # If v has been visited and it has the
                # same color as u
                elif color[v] == color[u]:
                    return False
        return True

    # This function returns the color assignment of vertices
    # if graph is Bipartite, else false
    def Bipartite(self):

        # Create a map to store colors assigned to all
        # vertices. The value '-1' is used to indicate
        # that no color is assigned to the vertex. The
        # value 1 is used to indicate first color is
        # assigned and value 0 indicates second color
        # is assigned.
        color = {v:-1 for v in self.graph.keys()}
        for v in color.keys():
            if color[v] == -1:
                if not self.BipartiteUtil(color, v):
                    return False
        return color