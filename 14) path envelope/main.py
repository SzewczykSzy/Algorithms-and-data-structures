import numpy as np


def jarvis_algorithm(tab):
    p = (np.inf, np.inf)
    for el in tab:
        if el[0] < p[0]:
            p = el
        elif el[0] == p[0]:
            if el[1] < p[1]:
                p = el
    p_idx = tab.index(p)
    p_start = p_idx
    result = []
    while True:
        q_idx = (p_idx + 1) % len(tab)
        for el in tab:
            sig = (tab[q_idx][1] - tab[p_idx][1]) * (el[0] - tab[q_idx][0]) - (el[1] - tab[q_idx][1]) * (
                    tab[q_idx][0] - tab[p_idx][0])
            if el == tab[p_idx]:
                continue
            elif sig > 0:
                q_idx = tab.index(el)
        result.append(tab[p_idx])
        p_idx = q_idx
        if p_idx == p_start:
            result.append(p)
            break
    return result


def jarvis_algorithm_1(tab):
    p = (np.inf, np.inf)
    for el in tab:
        if el[0] < p[0]:
            p = el
        elif el[0] == p[0]:
            if el[1] < p[1]:
                p = el
    p_idx = tab.index(p)
    p_start = p_idx
    result = []
    while True:
        q_idx = (p_idx + 1) % len(tab)
        for el in tab:
            sig = (tab[q_idx][1] - tab[p_idx][1]) * (el[0] - tab[q_idx][0]) - (el[1] - tab[q_idx][1]) * (
                        tab[q_idx][0] - tab[p_idx][0])
            d_1 = np.sqrt(((tab[p_idx][0] - el[0]) ** 2) + ((tab[p_idx][1] - el[1]) ** 2))
            d_2 = np.sqrt(((tab[q_idx][0] - el[0]) ** 2) + ((tab[q_idx][1] - el[1]) ** 2))
            if el == tab[p_idx]:
                continue
            elif sig > 0 or (sig == 0 and d_1 > d_2):
                q_idx = tab.index(el)
        result.append(tab[p_idx])
        p_idx = q_idx
        if p_idx == p_start:
            result.append(p)
            break
    return result


def main():
    tab_1 = [(0, 3), (0, 0), (0, 1), (3, 0), (3, 3)]
    tab_2 = [(0, 3), (0, 1), (0, 0), (3, 0), (3, 3)]
    print(jarvis_algorithm(tab_1))
    print(jarvis_algorithm_1(tab_1))
    print("")
    print(jarvis_algorithm(tab_2))
    print(jarvis_algorithm_1(tab_2))
    print("")
    tab_3 = [(2, 2), (4, 3), (5, 4), (0, 3), (0, 2), (0, 0), (2, 1), (2, 0), (4, 0)]
    print(jarvis_algorithm(tab_3))
    print(jarvis_algorithm_1(tab_3))


if __name__ == '__main__':
    main()
