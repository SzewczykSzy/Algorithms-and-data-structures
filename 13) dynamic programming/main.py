import numpy as np


def string_compare_rec(P, T, i, j):
    if i == 0:
        return j
    if j == 0:
        return i
    if P[i] != T[j]:
        change = string_compare_rec(P, T, i-1, j-1) + 1
    else:
        change = string_compare_rec(P, T, i-1, j-1)
    insert = string_compare_rec(P, T, i, j-1) + 1
    delete = string_compare_rec(P, T, i-1, j) + 1
    lowest_cost = min(change, insert, delete)
    return lowest_cost


def string_compare_pd(P, T, x, y):
    D = np.zeros((x, y))
    for k in range(x):
        for l in range(y):
            D[k, 0] = k
            D[0, l] = l
    parent = np.full((x, y), 'X')
    change = np.zeros((x, y))
    insert = np.zeros((x, y))
    delete = np.zeros((x, y))
    for i in range(x):
        for j in range(y):
            if P[i] != T[j]:
                change[i, j] = D[i-1, j-1] + 1
            else:
                change[i, j] = D[i-1, j-1]
            insert[i, j] = D[i, j-1] + 1
            delete[i, j] = D[i-1, j] + 1
            tab = [change[i, j], insert[i, j], delete[i, j]]
            D[i, j] = np.min(tab)
            idx_lowest_cost = np.argmin(tab)

            if P[i] == T[j]:
                parent[i, j] = 'M'
            elif idx_lowest_cost == 0:
                parent[i, j] = 'S'
            elif idx_lowest_cost == 1:
                parent[i, j] = 'I'
            elif idx_lowest_cost == 2:
                parent[i, j] = 'D'
    for k in range(1, x):
        for l in range(1, y):
            parent[0, l] = 'I'
            parent[k, 0] = 'D'
    return D[-1, -1]


def path_reproduction(P, T, x, y):
    D = np.zeros((x, y))
    for k in range(x):
        for l in range(y):
            D[k, 0] = k
            D[0, l] = l
    parent = np.full((x, y), 'X')
    change = np.zeros((x, y))
    insert = np.zeros((x, y))
    delete = np.zeros((x, y))
    for i in range(x):
        for j in range(y):
            if P[i] != T[j]:
                change[i, j] = D[i-1, j-1] + 1
            else:
                change[i, j] = D[i-1, j-1]
            insert[i, j] = D[i, j-1] + 1
            delete[i, j] = D[i-1, j] + 1
            tab = [change[i, j], insert[i, j], delete[i, j]]
            D[i, j] = np.min(tab)
            idx_lowest_cost = np.argmin(tab)

            if P[i] == T[j]:
                parent[i, j] = 'M'
            elif idx_lowest_cost == 0:
                parent[i, j] = 'S'
            elif idx_lowest_cost == 1:
                parent[i, j] = 'I'
            elif idx_lowest_cost == 2:
                parent[i, j] = 'D'
    for k in range(1, x):
        for l in range(1, y):
            parent[0, l] = 'I'
            parent[k, 0] = 'D'
    i = x - 1
    j = y - 1
    path = []
    while i > 0:
        path.append(parent[i, j])
        if parent[i, j] == 'D':
            i -= 1
        elif parent[i, j] == 'I':
            j -= 1
        elif parent[i, j] == 'M' or parent[i, j] == 'S':
            i -= 1
            j -= 1
    return path[::-1]


def match_substrings(P, T, x, y):
    D = np.zeros((x, y))
    for k in range(x):
        for l in range(y):
            D[k, 0] = k
    parent = np.full((x, y), 'X')
    change = np.zeros((x, y))
    insert = np.zeros((x, y))
    delete = np.zeros((x, y))
    for i in range(x):
        for j in range(y):
            if P[i] != T[j]:
                change[i, j] = D[i-1, j-1] + 1
            else:
                change[i, j] = D[i-1, j-1]
            insert[i, j] = D[i, j-1] + 1
            delete[i, j] = D[i-1, j] + 1
            tab = [change[i, j], insert[i, j], delete[i, j]]
            D[i, j] = np.min(tab)
            idx_lowest_cost = np.argmin(tab)

            if P[i] == T[j]:
                parent[i, j] = 'M'
            elif idx_lowest_cost == 0:
                parent[i, j] = 'S'
            elif idx_lowest_cost == 1:
                parent[i, j] = 'I'
            elif idx_lowest_cost == 2:
                parent[i, j] = 'D'
    for k in range(1, x):
        for l in range(0, y):
            parent[0, l] = 'X'
            parent[k, 0] = 'D'
    i = x - 1
    j = y - 1
    path = []
    while i > 0:
        path.append(parent[i, j])
        if parent[i, j] == 'D':
            i -= 1
        elif parent[i, j] == 'I':
            j -= 1
        elif parent[i, j] == 'M' or parent[i, j] == 'S':
            i -= 1
            j -= 1

    idx = (np.argmin(D[-1, 1:]) + 1) - (x - 1) + 1
    return idx


def longest_sequence(P, T, x, y):
    D = np.zeros((x, y))
    for k in range(x):
        for l in range(y):
            D[k, 0] = k
            D[0, l] = l
    parent = np.full((x, y), 'X')
    change = np.zeros((x, y))
    insert = np.zeros((x, y))
    delete = np.zeros((x, y))
    for i in range(1, x):
        for j in range(1, y):
            if P[i] != T[j]:
                change[i, j] = D[i - 1, j - 1] + 100
            else:
                change[i, j] = D[i - 1, j - 1]
            insert[i, j] = D[i, j - 1] + 1
            delete[i, j] = D[i - 1, j] + 1
            tab = [change[i, j], insert[i, j], delete[i, j]]
            D[i, j] = np.min(tab)
            idx_lowest_cost = np.argmin(tab)

            if P[i] == T[j]:
                parent[i, j] = 'M'
            elif idx_lowest_cost == 0:
                parent[i, j] = 'S'
            elif idx_lowest_cost == 1:
                parent[i, j] = 'I'
            elif idx_lowest_cost == 2:
                parent[i, j] = 'D'
    for k in range(1, x):
        for l in range(1, y):
            parent[0, l] = 'I'
            parent[k, 0] = 'D'
    i = x - 1
    j = y - 1
    path = []
    while i > 0:
        if parent[i, j] == 'D':
            i -= 1
        elif parent[i, j] == 'I':
            j -= 1
        elif parent[i, j] == 'M' or parent[i, j] == 'S':
            path.append(P[i])
            i -= 1
            j -= 1
    return path[::-1]



def main():
    P = ' kot'
    T = ' kon'
    print(string_compare_rec(P, T, len(P) - 1, len(T) - 1))
    P = ' kot'
    T = ' pies'
    print(string_compare_rec(P, T, len(P) - 1, len(T) - 1))
    P = ' biały autobus'
    T = ' czarny autokar'
    print(int(string_compare_pd(P, T, len(P), len(T))))
    P = ' thou shalt not'
    T = ' you should not'
    print(path_reproduction(P, T, len(P), len(T)))
    P = ' ban'
    T = ' mokeyssbanana'
    print(match_substrings(P, T, len(P), len(T)))
    P = ' democrat'
    T = ' republican'
    print(longest_sequence(P, T, len(P), len(T)))
    T = ' 243517698'
    P = sorted(T)
    print(longest_sequence(P, T, len(P), len(T)))


if __name__ == '__main__':
    main()
