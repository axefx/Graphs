"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
        self.path = []

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("nonexistent vert")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            v = q.dequeue()
            if v not in visited:
                visited.add(v)
                print(f"{v}")
                for next_vert in self.get_neighbors(v):
                    q.enqueue(next_vert)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()
        s.push(starting_vertex)
        while s.size() > 0:
            v = s.pop()
            if v not in visited:
                visited.add(v)
                print(f"{v}")
                for next_vert in self.get_neighbors(v):
                    s.push(next_vert)

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if visited == None:
            visited = set()
        visited.add(starting_vertex)
        print(f'{starting_vertex}')
        for next_vert in self.get_neighbors(starting_vertex):
            if next_vert not in visited:
                self.dft_recursive(next_vert, visited)
        # visited = set()
        # def dft_inner(vertex):
        #     if vertex in visited:
        #         return
        #     else:
        #         visited.add(vertex)
        #         print(f"{vertex}")
        #     for neighbor in self.get_neighbors(vertex):
        #         dft_inner(neighbor)

        # dft_inner(starting_vertex)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        # Create a Set to store visited vertices
        visited = set()
        q = Queue()
        q.enqueue([starting_vertex])
        # While the queue is not empty...
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_vertex = path[-1]
            # If that vertex has not been visited...
            if last_vertex not in visited:
                # CHECK IF IT'S THE TARGET
                if last_vertex == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_vertex)
            # Then add A PATH TO its neighbors to the back of the queue
            for neighbor in self.get_neighbors(last_vertex):
                # COPY THE PATH
                next_path = path[:]
                # APPEND THE NEIGHBOR TO THE BACK
                next_path.append(neighbor)
                q.enqueue(next_path)
        return None

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        visited = set()
        s = Stack()
        s.push([starting_vertex])
        while s.size() > 0:
            path = s.pop()
            last_vertex = path[-1]
            if last_vertex not in visited:
                visited.add(last_vertex)
            for neighbor in self.get_neighbors(last_vertex):
                next_path = path[:]
                next_path.append(neighbor)
                if neighbor == destination_vertex:
                    return next_path
                s.push(next_path)

    def dfs_recursive(self, v, destination_vertex,path = None, visited=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        if visited == None:        # if visited doesnt exist create it
            visited = set()
        if path == None:             # if path doesnt exist create it
            path = []
        visited.add(v)              # add current node to visited
        path = path + [v]           # add current node to path
        if v == destination_vertex:      # if current node is destination 
            return path                  # return the path
        for vertex in self.vertices[v]:          # find the next node 
            if vertex not in visited:             # if next node is not in visited

                new_path = self.dfs_recursive(vertex, destination_vertex, path, visited)            # create new path
                if new_path != None:                                         # if new path is not at the end
                    return new_path                                         # return the new path
        ####
        # visited = set()

        # def dft_inner(path):
        #     last_vertex = path[-1]
            
        #     if last_vertex in visited:
        #         return None
        #     else:
        #         visited.add(last_vertex)

        #     if last_vertex == destination_vertex:
        #         return path
            
        #     for neighbor in self.get_neighbors(last_vertex):
        #         next_path = path.copy()
        #         next_path.append(neighbor)
            
        #         found = dft_inner(next_path)
        #         if found:
        #             return found
            
        #     return None

        # return dft_inner([starting_vertex])
        ####
        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # for neighbor in self.get_neighbors(starting_vertex):
        #     if neighbor not in path:
        #         if neighbor == destination_vertex:
        #             return path + [neighbor]
        #         path = self.dfs_recursive(neighbor, destination_vertex, path)
        
        # return path

        # if visited is None:
        #     visited = set()
        # if path is None:
        #     path = []
        # visited.add(starting_vertex)
        # path.append(starting_vertex)
        # if starting_vertex == destination_vertex:
        #     return path

        # for next_vert in self.get_neighbors(starting_vertex):
        #     if next_vert not in visited:
        #         return self.dfs_recursive(next_vert, destination_vertex, visited, path)

        # return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    # graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    # graph.dft(1)
    # graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    # print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
