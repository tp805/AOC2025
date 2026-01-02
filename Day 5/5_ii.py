ranges = []

with open("Day 5/in.txt", "r") as file:
    for line in file:
        l,u = map(int,line.strip().split('-'))
        ranges.append([l,u])


ranges.sort(key = lambda x: x[0])

left = 0
right = -1
ans=0

for i in ranges:
    if i[0] <= right:
        right = max(right,i[1])
    elif i[0] > right:
        ans += right-left+1
        left = i[0]
        right = i[1]

ans += right-left+1

print(ans)