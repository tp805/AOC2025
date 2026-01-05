nums = []
ops = []

with open("Day 6/in.txt","r") as file:
    for line in file:
        if '*' in line or '+' in line:
            ops = line.strip().split()
        else:
            line_nums = list(map(int,line.strip().split()))
            nums.append(line_nums)
        
ans = 0

for i in range(len(ops)):
    if ops[i] == '*':
        prod = 1
        for j in nums:
            prod *= j[i]
        ans += prod
    
    elif ops[i] == '+':
        sum = 0
        for j in nums:
            sum += j[i]
        ans += sum

print(ans)