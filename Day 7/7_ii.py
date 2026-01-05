m = []
cnt = 0
with open("Day 7/in.txt","r") as file:
    for line in file:
        m.append(list(line))

for i in range(len(m[0])):
    if m[0][i] == 'S':
        m[0][i] = 1
        break

for i in range(1, len(m)):
    for j in range(len(m[i])):
        if type(m[i-1][j]) is int:
            if m[i][j] == '^':
                if m[i][j-1] == '.':
                    m[i][j-1] = 0
                if m[i][j+1] == '.':
                    m[i][j+1] = 0
                m[i][j-1] += m[i-1][j]
                m[i][j+1] += m[i-1][j]
            else:
                if m[i][j] == '.':
                    m[i][j] = 0
                m[i][j] += m[i-1][j]

for i in m[-1]:
    if type(i) is int:
        cnt += i
print(cnt)