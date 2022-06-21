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

# helpers 
def get_shortest_distance(table, vertex):
    shortest_distance = table[vertex][DISTANCE]
    return shortest_distance

def set_shortest_distance(table, vertex, new_distance):
    table[vertex][DISTANCE] = new_distance
    
def set_previous_node(table, vertex, previous_node):
    table[vertex][PREVIOUS_NODE] = previous_node
    
def get_distance(graph, first_vertex, second_vertex):
    return graph[first_vertex][second_vertex]

def get_next_node(table, visited_nodes):
    unvisited_nodes = list(set(table.keys()).difference(set(visited_nodes)))
    assumed_min = table[unvisited_nodes[0]][DISTANCE]
    min_vertex = unvisited_nodes[0]
    for node in unvisited_nodes:
        if table[node][DISTANCE] < assumed_min:
            assumed_min = table[node][DISTANCE]
            min_vertex = node
    return min_vertex
    

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
                
                if distance_from_starting_node == INFINITY and current_node == starting_node:
                    total_distance = get_distance(graph, vertex, current_node)
                else:
                    total_distance = get_shortest_distance(table, current_node) + get_distance(graph, current_node, vertex)
                
                if total_distance < distance_from_starting_node:
                    set_shortest_distance(table, vertex, total_distance)
                    set_previous_node(table, vertex, current_node)
                    
        visited_node.append(current_node)
            
        if len(visited_node) == len(table.keys()):
            break
        current_node = get_next_node(table, visited_node)
            
            
        shortest_distance_table = find_shortest_path(graph, table, 'A')
        for k in sorted(shortest_distance_table):
            print(f'{k}, {shortest_distance_table[k]}')