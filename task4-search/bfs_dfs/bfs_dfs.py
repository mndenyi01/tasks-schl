from collections import deque

def Bfs(graph, start, goal):
    if start == goal:
        return [start] # Terminate, to save on memory and time.
    queue = deque([[start]]) # Queue stores the path to the current node
    visited = set()

    while queue:
        path = queue.popleft() # Get the first path from the queue
        node = path[-1] # Get the last node from that path

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            # Explore neighbors and build new paths
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    
    return "Goal not reachable"

def Dfs(graph, start, goal):
    if start == goal:
        return [start] # Terminate, to save on memory and time.
    stack = [[start]] # Stack stores the path
    visited = set()

    while stack:
        path = stack.pop() # Get the last/recent path added
        node = path[-1] # Get the last node from that path

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)
            # Explore neighbors and build new paths
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)

    return "Goal not reachable"


# Example Graphs
simple_graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [], 
    'F': []
}
complex_graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E'],
    'C': ['B', 'G'],
    'D': ['F'],
    'E': ['C', 'H'],
    'F': ['Z'],
    'G': ['Z'],
    'H': ['Z'],
    'Z': []
}

print(f"BFS Path for simple graph,A to F: {Bfs(simple_graph, 'A', 'F')}")
print(f"BFS Path for complex graph,A to Z: {Bfs(complex_graph, 'A', 'Z')}")

print(f"DFS Path for simple graph,A to F: {Dfs(simple_graph, 'A', 'F')}")
print(f"DFS Path for complex graph,A to Z: {Dfs(complex_graph, 'A', 'Z')}")