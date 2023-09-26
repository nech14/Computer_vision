

def get_x_y(file):
    buf = []
    with open(file, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            buf.append(line.split())

    x = 0
    y = 0
    for i in range(len(buf)):
        for j in range(len(buf[0])):
            if buf[i][j] == '1':
                x = i
                y = j
                return(x, -y)

def get_offset(file1, file2):
    x1, y1 = get_x_y(file1)
    x2, y2 = get_x_y(file2)
    return x1-x2, y1-y2



def norm_resol(file):
    mas = []
    n = 0
    ml = 0
    bl = 0
    with open(file, 'r') as f:
        n = float(f.readline())
        f.readline()
        for line in f:
            mas.append(line.split())

    for i in range(len(mas)):
        bl = 0
        for j in range(len(mas[0])):
            mas[i][j] = int(mas[i][j])
            bl += mas[i][j]
        if ml < bl:
            ml = bl

    if n > 0 and ml > 0:
        return n/ml
    else:
        return 'unknown'


file = 'figure'
mnfile = 6
for i in range(1, mnfile+1):
    namefile = file + str(i) + '.txt'
    print(file + str(i) + ':', norm_resol(namefile))



file1 = 'img1.txt'
file2 = 'img2.txt'

print(file1 + ' offset ' + file2 + ':', get_offset(file1, file2))



