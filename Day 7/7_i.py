m = []
cnt = 0
with open("Day 7/in.txt","r") as file:
    for line in file:
        m.append(list(line))

for i in range(len(m[0])):
    if m[0][i] == 'S':
        m[0][i] = '|'
        break

for i in range(1, len(m)):
    for j in range(len(m[i])):
        if m[i-1][j] == '|':
            if m[i][j] == '^':
                cnt += 1
                m[i][j-1] = '|'
                m[i][j+1] = '|'
            else:
                m[i][j] = '|'

print(cnt)

with open ("Day 7/out_i.txt", "w") as f:
    for i in m:
        f.write(''.join(i))