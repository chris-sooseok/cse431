def BFS(n, m, s, t, edges):

    result = "no"
    layer = float("inf")

    if s == t:
        result = "yes"
        layer = 0
        return result, layer

    # input sanity checks
    #* s or t can't exceed the given number of vertices
    if s > n or t > n:
        return result, layer
    
    #* s or t can't be lower than or equal to 0
    if s <= 0 or t <= 0:
        return result, layer
    
    #* n and m can't be lower than 1
    if n < 1 or m < 1:
        return result, layer
    
    # * number of edges should be equal to m
    if len(edges) != m:
        return result, layer
    
    # layers to mark a layer for each vertex being explored
    #* this also helps marking explored notes
    layers = {s: 0} 
    # q to explore each vertex one by one
    #* starts with s
    q = [s]

    # loop until there is no vertex to explore
    while len(q) != 0:

        # find all unexplored neighbors of v
        v = q.pop(0)
        for edge in edges:
            u = None
            if v == edge[0]:
                u = edge[1]
            elif v == edge[1]:
                u = edge[0]
            # if a ngb u is found, and not explored yet
                #* add a layer to that neighbor from the current exploring node
                #* append the neighbor to the queue to explore its neighbors as well
            if u is not None and u not in layers:
                layers[u] = layers[v] + 1
                q.append(u)
                # if the neighbor is t, we have found the destination node
                    #* we have marked its layer above, so we are safe to break
                    #* update the return values
                if u == t:
                    layer = layers[t]
                    result = "yes"
                    return result, layer
    
    # by this point, the node t is not found since we return immediately once t is found during the exploration
    return result, layer


def read_input():
    n, m = map(int, input().split())
    s, t = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
    return n, m, s, t, edges


if __name__ == "__main__":
    n, m, s, t, edges = read_input()
    result, layer = BFS(n, m, s, t, edges)
    print(result)
    print(layer)
