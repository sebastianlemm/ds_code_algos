def extract_min(verts):
    min_index = 0
    for v in range(1, len(verts)):
        if verts[v][1] < verts[min_index][1]:
            min_index = v
    return verts.pop(min_index)

def prim_mst(graph):
    n_verts = len(graph)
    verts_to_process = [[i, float("inf"), -1] for i in range(n_verts)]  # Adding parent information
    verts_to_process[0][1] = 0  # Start from vertex 0
    
    mst_edges = []

    while verts_to_process:
        u = extract_min(verts_to_process)
        if u[2] != -1:
            mst_edges.append([u[0], u[2]])  # Add edge to MST only if it's not the starting vertex

        for v in verts_to_process:
            if graph[u[0]][v[0]] > 0 and graph[u[0]][v[0]] < v[1]:
                v[1] = graph[u[0]][v[0]]
                v[2] = u[0]  # Set the parent of vertex v

    return mst_edges

# Adjacency matrix representation of a graph
graph = [[0, 7, 0, 0, 0, 10, 15, 0],
         [7, 0, 12, 5, 0, 0, 0, 9],
         [0, 12, 0, 6, 0, 0, 0, 0],
         [0, 5, 6, 0, 14, 8, 0, 0],
         [0, 0, 0, 14, 0, 3, 0, 0],
         [10, 0, 0, 8, 3, 0, 0, 0],
         [15, 0, 0, 0, 0, 0, 0, 0],
         [0, 9, 0, 0, 0, 0, 0, 0]]

mst = prim_mst(graph)
print(mst)

## Output ## 
## [[1, 0], [3, 1], [2, 3], [5, 3], [4, 5], [7, 1], [6, 0]] ##