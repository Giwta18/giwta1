def pair(lst, t):
    l = []
    for j in range(len(lst)):
        for k in range(len(lst)):
            if j == k:
                continue

            s = lst[j] + lst[k]
            if s == t:
                l.append(lst[j])
                l.append(lst[k])

    coll = set(l)
    j = 0
    while j < len(lst):
        if lst[j] in coll:
            lst.pop(j)
            j -= 1
        j += 1

