graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [6],
    5: [1],
    6: [2]
}

# Recursive Solution

# runtime complexity: O(V + E)
# space complexity: O(V + E)
def reverseGraphR(graph):
   
    g = graph
    visited = set()
    def dfs(node):
        if node not in visited:
            visited.add(node)
            for _ in range(len(g[node])):
                n = g[node].pop(0)
                dfs(n)
                g[n].append(node)
    
    for n in graph:
        if n not in visited:
            dfs(n)
       
    return g
    
# runtime complexity: O(V + E)
# space complexity: O(V +E)

def reverseGraphI(graph):
    
    reversedGraph = {vertex: [] for vertex in graph}
    
    for source, neighbors in graph.items():
        for target in neighbors:
            reversedGraph[target].append(source)
            
    return reversedGraph

print(reverseGraphR(graph))
print(reverseGraphI(graph))