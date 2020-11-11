import numpy as np


# Representation of Nodes
# S: 0 ,  C: 1 ,  E: 2 ,  H: 3 ,  F: 4 ,  D: 5 ,  G: 6 ,  B: 7 ,  A: 8

INF = 99999999 # Infinity

Graph = np.array([[ 0,  3,   2,   1,   INF, INF, INF, INF, INF],
                  [ 3,  0,   1,   INF, 3,   2,   INF, INF, INF],
                  [ 2,  1,   0,   1,   INF, INF, INF, INF, INF],
                  [ 1,  INF, 1,   0,   2,   INF, INF, 5,   INF],
                  [INF, 3,   INF, 2,   0,   2,   INF, 3,   INF],
                  [INF, 2,   INF, INF, 2,   0,   1,   INF, 5  ],
                  [INF, INF, INF, INF, INF, 1,   0,   1,   2  ],
                  [INF, INF, INF, 5,   3,   INF, 1,   0,   4  ],
                  [INF, INF, INF, INF, INF, 5,   2,   4,   0  ]])

def floyd_warshall(Distance_Matrix, node):
    for k in range(node):
        for i in range(node):
            for j in range(node):
                Distance_Matrix[i][j] = min(Distance_Matrix[i][j], Distance_Matrix[i][k] + Distance_Matrix[k][j])
    return Distance_Matrix

print(floyd_warshall(Graph, 9))
print("\nShortest Path's Length Between A and S: ", floyd_warshall(Graph, 9)[0][8])
