import numpy as np


# Representation of Nodes
# A: 0 ,  B: 1 ,  C: 2 ,  D: 3 ,  E: 4 ,  F: 5 ,  G: 6 ,  H: 7 ,  S: 8

INF = 99999999 # Infinity

Graph = np.array([[0, 4, INF, 5, INF, INF, 2, INF, INF],
                 [4, 0, INF, 5, INF, INF, 1, 5, INF],
                 [INF, INF, 0, 2, 1, 3, INF, INF, 3],
                 [5, INF, 2, 0, INF, 2, 1, INF, INF],
                 [INF, INF, 1, INF, 0, INF, 2, INF, INF],
                 [INF, 3, 3, 2, INF, 0, INF, 2, INF],
                 [INF, INF, 1, INF, INF, INF, INF, 1, 2],
                 [INF, INF, INF, INF, 1, 2, INF, 0, 1],
                 [INF, INF, 3, INF, 2, INF, INF, 1, 0]])

def floyd_warshall(Distance_Matrix, node):
    for k in range(node):
        for i in range(node):
            for j in range(node):
                Distance_Matrix[i][j] = min(Distance_Matrix[i][j], Distance_Matrix[i][k] + Distance_Matrix[k][j])
    return Distance_Matrix

print(floyd_warshall(Graph, 9))
print("\nShortest Path's Length Between A and S: ", floyd_warshall(Graph, 9)[0][8])
