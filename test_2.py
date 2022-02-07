def way(i, j):
    coords = []
    if i < leni - 1:
        coords.append([i + 1, j])
    if i > 0:
        coords.append([i - 1, j])
    if j > 0:
        coords.append([i, j - 1])
    if j < lenj - 1:
        coords.append([i, j + 1])

    returnarr = []
    if coords == []:
        return returnarr
    #print(coords)
    for item in coords:
        try:
            if a[item[0]][item[1]] > a[i][j]:
                returnarr.append([item[0], item[1]])
        except:
            pass
            #print(item, i, j)

    return returnarr

def path(coord, n):
    loc = way(coord[0], coord[1]) # len = 3
    #print(n)
    if loc == []:
        return n
    else:
        le = 0

        for item in loc:
            locle = path(item, n + 1)
            if locle > le:
                le = locle

        return le

with open('test.txt') as f:
    a = list(map(lambda x: list(map(int, x.replace('\t', ' ').split())), f.read().split('\n')))

leni = len(a)
lenj = len(a[0])
maxle = 0

for i in range(leni):
    for j in range(lenj):
        le = 0

        loc = way(i, j) #len = 1

        if loc == [[11, 4], [9, 4], [10, 3], [10, 5]]:
            print('here')

        for item in loc:
            #print(item) # len = 2
            locle = path(item, 2)
            if locle > le:
                le = locle

        if le > maxle:
            maxle = le
        #print(le)

print(maxle)
