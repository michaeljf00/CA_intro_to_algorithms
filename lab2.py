# Lab 2


# Question 2c
from collections import deque

# runtime complexity: O(n^d)
# space complexity: O(n^d)
def pourWater():
        
    queue = deque([((0, 4, 7), [])])
    capacity = [10, 4, 7]
    
    visited = set()
    paths = []
    while queue:
        state, path = queue.popleft()
        
        if state in visited:
            continue
        
        visited.add(state)
        if state[1] == 2 or state[2] == 2:
            paths.append(path)
        
        for i in range(3):
            for j in range(3):
                if i != j:
                    pour = min(state[i], capacity[j] - state[j])
                    
                    new_state = list(state)
                    new_state[i] -= pour
                    new_state[j] += pour
                    
                    new_path = path + [(i, j, pour)]
                    queue.append((tuple(new_state), new_path))
                    
    return paths
        
for path in pourWater():
    print(path)

graph1 = [
    (1, 2),
    (1, 3),
    (2, 4),
    (3, 5),
    (4, 5),
]

# Question 3
def findCycle(graph):
    length = -1
    for edge in graph:
        length = max(length, edge[0], edge[1])
    
    length += 1  # Increment length to include the node with the maximum index
    matrix = [[0 for _ in range(length)] for _ in range(length)]

    for edge in graph:
        matrix[edge[0] - 1][edge[1] - 1] = 1
        matrix[edge[1] - 1][edge[0] - 1] = 1  # Add the reverse edge for undirected graph
    
    visited = set()
    
    def dfs(node, parent):
        if node in visited:
            return True
            
        visited.add(node)
        
        hasCycle = False
        for i in range(length):
            if i != parent and matrix[node][i] == 1:
                hasCycle = hasCycle or dfs(i, node)
                
        return hasCycle
        
    cycleLocated = False
    for i in range(length):
        if i not in visited:
            cycleLocated = cycleLocated or dfs(i, None)
        
    return cycleLocated

# Example usage:
graph = [(1, 2), (2, 3), (3, 1)]
result = findCycle(graph)
print(result)  # Output: True
                    
