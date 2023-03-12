def naive_method(S, W):
    num_of_idx = []
    m = 0
    while m < len(S):
        if S[m] != W[0]:
            m += 1
        elif S[m] == W[0]:
            m += 1
            idx = 0
            for j in W:
                if j == S[m + idx - 1]:
                    if idx == len(W) - 1:
                        num_of_idx.append(m - idx)
                    idx += 1
                else:
                    break
    return len(num_of_idx), m


def rabin_karp_method(S, W):
    hW = hash(W)
    i = 0
    compare = 0
    collision = 0
    for m in range(len(S) - len(W)):
        hS = hash(S[m:m+len(W)])
        compare += 1
        if hS == hW:
            if S[m:m+len(W)] == W:
                i += 1
            else:
                collision += 1
    return i, compare, collision


def rabin_karp_rolling_method(S, W):
    hW = hash(W)
    i = 0
    compare = 0
    collision = 0
    d = 256
    q = 101
    h = 1
    for j in range(len(W)):
        h = (h * d) % q
    hS = hash(S[:len(W)])
    for m in range(len(S) - len(W) + 1):
        compare += 1
        if hS == hW:
            if S[m:m + len(W)] == W:
                i += 1
            else:
                collision += 1
        if m != len(S) - len(W):
            hS = (d * hS - ord(S[m]) * h + ord(S[m + len(W)])) % q
            if hS < 0:
                hS += q
    return i, compare, collision


def hash(word):
    hw = 0
    for i in range(len(word)):
        hw = (hw * 256 + ord(word[i])) % 101
    return hw


def knuth_morris_pratt(S, W):
    m = 0
    i = 0
    T = kmp_table(W)
    nP = 0
    P = []
    count = 0
    while m < len(S):
        count += 1
        if W[i] == S[m]:
            m += 1
            i += 1
            if i == len(W):
                P.append(m-i)
                nP += 1
                i = T[i]
        else:
            i = T[i]
            if i < 0:
                m += 1
                i += 1
    return nP, count


def kmp_table(W):
    pos = 1
    cnd = 0
    T = [0 for i in range(len(W) + 1)]
    T[0] = -1
    while pos < len(W):
        if W[pos] == W[cnd]:
            T[pos] = T[cnd]
        else:
            T[pos] = cnd
            while cnd >= 0 and W[pos] != W[cnd]:
                cnd = T[cnd]
        pos += 1
        cnd += 1
    T[pos] = cnd
    return T


def main():
    with open("lotr.txt", encoding='utf8') as f:
        txt = f.readlines()
    S = ''.join(txt).lower()
    template = 'time.'
    W = ''.join(template).lower()

    num, compare = naive_method(S, W)
    print("{0} ; {1}".format(num, compare))

    num_2, compare_2, collision_2 = rabin_karp_rolling_method(S, W)
    print("{0} ; {1} ; {2}".format(num_2, compare_2, collision_2))

    num_3, compare_3 = knuth_morris_pratt(S, W)
    print("{0} ; {1}".format(num_3, compare_3))


if __name__ == '__main__':
    main()
