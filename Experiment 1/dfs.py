def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    print(start, end=" ")
    visited.add(start)

    if start in graph:
        for neighbor in graph[start]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))

    for _ in range(vertices):
        vertex = int(input("Enter the vertex: "))
        adjacent_vertices = list(map(int, input("Enter adjacent vertices for vertex " + str(vertex) + ": ").split()))
        graph[vertex] = adjacent_vertices
        print("\n")

    return graph

graph = create_graph()

start_vertex = int(input("\nEnter the start vertex for DFS: "))

print("\n\n")
print("For graph: \n", graph)
print("\n")
print("DFS Traversal is: ")
dfs(graph, start_vertex)
