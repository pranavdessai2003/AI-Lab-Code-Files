def bfs(graph, start):
    visited = set()
    queue = [start]
    visited.add(start)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        if vertex in graph:
            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)



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

start_vertex = int(input("\nEnter the start vertex for BFS: "))

print("\n\n")
print("For graph: \n " , graph)
print("\n")
print("BFS Traversal is: ")
bfs(graph, start_vertex)
