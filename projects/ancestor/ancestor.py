class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
    def size(self):
        return len(self.queue)

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def get_parents(self, vertex_id):
        return self.vertices[vertex_id]

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    q = Queue()

    for (parent, child) in ancestors:
        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)

        g.add_edge(child, parent)
    
    q.enqueue(starting_node)
    earliest = -1
    visited = set()

    while q.size():
        curr_node = q.dequeue()
        if curr_node not in visited:
            visited.add(curr_node)
            parents = g.get_parents(starting_node)
            for (i, parent) in enumerate(parents):
                q.enqueue(parent)
                if i == 0:
                    earliest = parent
                elif parent < earliest:
                    earliest = parent 

    return earliest
