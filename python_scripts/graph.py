'''Graphs and Other Algorithms'''


from collections import deque


graph = dict()
graph['A'] = ['B', 'C']
graph['B'] = ['E','A']
graph['C'] = ['A', 'B', 'E','F']
graph['E'] = ['B', 'C']
graph['F'] = ['C']
# Adjacency matrix
# matrix is a two-dimensional array
matrix_elements = sorted(graph.keys())
cols = rows = len(matrix_elements)
adjacency_matrix = [[0 for x in range(rows)] for y in range(cols)]
edges_list = []


# The multidimensional array is filled using a nested for loop:
for key in matrix_elements:
    for neighbor in graph[key]:
        edges_list.append((key,neighbor))
        print(edges_list)
        
        # What needs to be done now is to fill the our 
        # multidimensional array by using 1 to mark the
        # presence of an edge with the line
  
for edge in edges_list:
    index_of_first_vertex = matrix_elements.index(edge[0])
    print(index_of_first_vertex)
    index_of_second_vertex = matrix_elements.index(edge[1])
    print(index_of_second_vertex)
    adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1
adjacency_matrix[index_of_first_vertex][index_of_second_vertex] = 1


# Breadth-first search
graph = dict()
graph['A'] = ['B','G', 'D']
graph['B'] = ['A','F', 'E']
graph['C'] = ['F','H']
graph['D'] = ['F','A']
graph['E'] = ['B','G']
graph['F'] = ['B','D', 'C']
graph['G'] = ['A','E']
graph['H'] = ['C']

from collections import deque


def breadth_first_search(graph, root):
    visited_vertices = list()
    graph_queue = deque([root])
    visited_vertices.append(root)
    node = root
    
    while len(graph_queue) > 0:
       node = graph_queue.popleft()
       adj_node = graph[node]
       remaining_elements = set(adj_node).difference(set(visited_vertices))
       if len(remaining_elements) > 0:
           for elem in sorted(remaining_elements):
               visited_vertices.append(elem)
               graph_queue.append(elem)
    return visited_vertices

# Depth-first search
def depth_first_search(graph, root):
    visited_vertices = list()
    graph_stack = list()
    
    graph_stack.append(root)
    node = root
    while len(graph_stack) > 0:
        if node not in visited_vertices:
            visited_vertices.append(node)
        adj_nodes = graph[node]
        if set(adj_nodes).issubset(set(visited_vertices)):
            graph_stack.pop()
        if len(graph_stack) > 0:
            node = graph_stack[-1]
            continue
        else:
            remaining_elements = set(adj_nodes).difference(set(visited_vertices))
            first_adj_node = sorted(remaining_elements)[0]
            graph_stack.append(first_adj_node)
            node = first_adj_node
            return visited_vertices
        
        ''' Depth-first searches find application in solving maze problems, finding connected
            components, and finding the bridges of a graph, among others. '''
