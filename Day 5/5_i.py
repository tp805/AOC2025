ranges = []
ans = 0
with open("Day 5/in.txt", "r") as file:
    for line in file:
        if '-' in line:
            l,u = map(int,line.strip().split('-'))
            ranges.append([l,u])
        elif line.strip():
            num = int(line.strip())
            for i in ranges:
                if num>=i[0] and num<=i[1]:
                    ans += 1
                    break

print(ans)