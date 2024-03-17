def create_graph():
    graph = {}
    vertices = int(input("Enter the number of vertices: "))

    for _ in range(vertices):
        vertex = int(input("Enter the vertex: "))
        adjacent_vertices = list(map(int, input("Enter adjacent vertices for" + str(vertex) + ": ").split()))
        graph[vertex] = adjacent_vertices

    return graph



graph = create_graph()
