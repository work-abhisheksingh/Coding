# DFS using recursion

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = set()  # To track visited nodes

def dfs(node):
    if node not in visited:
        print(node, end=" ")    # Process the node
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor)

# Run DFS starting from node 'A'
dfs('A')
