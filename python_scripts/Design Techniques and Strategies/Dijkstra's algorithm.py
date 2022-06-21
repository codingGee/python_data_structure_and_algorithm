'''Dijkstra's algorithm'''



table = dict()
table = {
    'A': [0, None],
    'B': [float('inf'),None],
    'B': [float('inf'),None],
    'D': [float('inf'),None],
    'E': [float('inf'),None],
    'F': [float('inf'),None],
}

DISTANCE = 0
PREVIOUS_NODE = 1
INFINITY = float('inf')

def find_shortest_path(graph, table, origin):
    visited_node = []
    current_node = origin
    starting_node = origin
    
    while True:
        adjacent_nodes = graph[current_node]
        if set(adjacent_nodes).issubset(set(visited_node)):
            # Nothing to do here all adjacent node has been visisted 
            pass
        else:
            unvisited_node = set(adjacent_nodes).difference(set(visited_node))
            
            for vertex  in unvisited_node:
                
                distance_from_starting_node = get_shortest_distance(table, vertex)