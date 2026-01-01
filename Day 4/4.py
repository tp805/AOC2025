def count_surround(x, y):
    global map
    cnt = 0
    direc = [[-1,-1], [-1,0], [-1,1], [0,-1], [0,1], [1,-1], [1,0], [1,1]]
    for i in direc:
        newx = x + i[0]
        newy = y + i[1]

        if newx>=0 and newx<len(map) and newy>=0 and newy<len(map[0]):
            if map[newx][newy] == "@":
                cnt += 1
    return cnt

map = []

with open("Day 4/in.txt", "r") as file:
    for line in file:
        map.append(list(line.replace("\n","")))

sum = 0
remove = 1
while remove > 0:
    remove = 0
    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == ".":
                continue
            count_ij = count_surround(i,j)
            if count_ij < 4:
                remove += 1
                map[i][j] = "."

    sum += remove

print(sum)
