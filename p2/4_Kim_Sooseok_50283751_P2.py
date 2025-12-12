
import heapq

def dijksta(n, m, edges):
    to_explore = set(range(1, n+1))
    # set 1 to 0 and 1001 otherwise
    d = {v:0 if v == 1 else 1001 for v in range(1, n+1)}
    q = []
    for v in range(1, n+1):
        heapq.heappush(q, (d[v], v))
    pars = {v:None for v in range(1, n+1)}
    
    while to_explore:
        d_of_u, u = heapq.heappop(q)
        # if 2 in q, then, the shortest path to 2 is already determined
        if u == 2: break
        if u not in to_explore:
            continue
        to_explore.remove(u)
        if u in edges:
            for v, w in edges[u].items():
                # current weight of u + weight of edge(u,v) < current distance of v
                if d_of_u + w < d[v]:
                    d[v] = d_of_u + w
                    heapq.heappush(q, (d[v], v))
                    pars[v] = u
    
    if pars[2] is None:
        return "INFINITY"
    
    total_weight = 0
    v = 2
    while pars[v] != None:
        par = pars[v]
        total_weight += edges[par][v]
        v = par
    return total_weight


def read_input():
    n, m = map(int, input().split())
    # creaing directional graph {u: [(v,w)]} so that it is easy to access neigbors of u and its weight
    edges = {}
    for _ in range(m):
        u, v, w = map(int, input().split())    
        if u not in edges:
            edges[u] = {}
        edges[u][v] = w
    return n, m, edges

if __name__ == "__main__":
    n, m, edges = read_input()
    result = dijksta(n, m, edges)
    print(result)