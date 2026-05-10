# This code was used in the CAT1 .
import heapq

def a_star_search(graph, start, goal, heuristics):
    """
    Implements A* search algorithm.
    :param graph: Graph adjacency list {node: [(neighbor, cost)]}
    :param start: Starting node
    :param goal: Target node
    :param heuristics: Dictionary of estimated costs from node to goal {node: cost}
    """
    # Priority Queue: (priority, current_node, path, total_g_cost)
    # priority = g_cost + heuristic
    frontier = [(heuristics[start], start, [start], 0)]
    visited = set()

    while frontier:
        # Pop the node with the lowest f(n)
        _, current_node, path, g_cost = heapq.heappop(frontier)

        if current_node in visited:
            continue
        
        # Goal test
        if current_node == goal:
            return path, g_cost

        visited.add(current_node)

        for neighbor, weight in graph.get(current_node, []):
            if neighbor not in visited:
                new_g_cost = g_cost + weight
                f_cost = new_g_cost + heuristics.get(neighbor, float('inf'))
                heapq.heappush(frontier, (f_cost, neighbor, path + [neighbor], new_g_cost))

    return None, float('inf')

# --- Example Usage ---

# Graph connections: (neighbor, edge_weight)
map_graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 4)],
    'C': [('E', 1)],
    'D': [('F', 2)],
    'E': [('F', 5)],
    'F': []
}

# Heuristic values (Straight-line distance to 'F')
h_values = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 2,
    'F': 0
}

path, cost = a_star_search(map_graph, 'A', 'F', h_values)

print(f"Optimal Path: {path}")
print(f"Total Resource Cost: {cost}")