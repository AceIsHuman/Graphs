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
    
    q.enqueue([starting_node])
    earliest = -1
    visited = set()
    highest_gen_length = 0

    while q.size():
        path = q.dequeue()
        curr_node = path[-1]
        if curr_node not in visited:
            visited.add(curr_node)
            parents = g.get_parents(curr_node)
            for parent in parents:
                if parent not in visited:
                    parent_path = path + [parent]
                    q.enqueue(parent_path)

                    if (len(parent_path) > highest_gen_length):
                        earliest = parent
                        highest_gen_length = len(parent_path)
                    elif (len(parent_path) == highest_gen_length) and (parent < earliest):
                        earliest = parent

    return earliest
