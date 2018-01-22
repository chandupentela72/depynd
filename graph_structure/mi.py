import numpy as np
from .mutual_information import knn
from .mutual_information import dr

def mimat(X, method=None, is_discrete=None, k=3):
    n, d = X.shape
    mis = np.eye(d)
    for i, j in [(i, j) for i in range(d) for j in range(d) if i != j]:
        x = X[:, [i]]
        y = X[:, [j]]
        if method == 'dr':
            mis[i, j] = dr.mi_knn(x, y)
        else:
            mis[i, j] = knn.mi_dir(x, y, k=3)

    mis[mis < 0] = 0
    mis[np.eye(d, dtype=bool)] = np.nan
    return mis


