
from disjoint_set import DisjointSet

def merge_sort(edges, length):
    if length == 1:
        return edges
    else:
        mid = length // 2
        B = merge_sort(edges[:mid], mid)
        C = merge_sort(edges[mid:], length - mid)
        return merge(B, C, mid, length - mid)

def merge(B, C, ln, rn):
    sorted_edges = []
    i = 0
    j = 0
    while i < ln and j < rn:
        if B[i][2] <= C[j][2]:
            sorted_edges.append(B[i])
            i += 1
        else:
            sorted_edges.append(C[j])
            j += 1
    if i < ln:
        for n in B[i:]:
            sorted_edges.append(n)
    if j < rn:
        for n in C[j:]:
            sorted_edges.append(n)
    return sorted_edges

def msf_kruskal(n, m, k, edges):
    djs = DisjointSet.from_iterable([i for i in range(1, n+1)])
    sorted_edges = merge_sort(edges, m)
    total_weight = 0
    for edge in sorted_edges:
        u, v, w = edge    
        if not djs.connected(u, v):
            djs.union(u, v)
            total_weight += w
            if len(list(djs.itersets())) == k:
                break
    
    return total_weight
    
def read_input():
    n, m, k = map(int, input().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    return n, m, k, edges

if __name__ == "__main__":
    n, m, k, edges = read_input()
    total_weight = msf_kruskal(n, m, k, edges)
    print(total_weight)

