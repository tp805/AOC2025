s = []
with open("Day 6/in.txt", "r") as file:
    for line in file:
        s.append(line.rstrip('\n'))

ans = 0
temp_nums = []
for j in range(len(s[0])-1, -1, -1):
    temp_string = ""
    for i in range(len(s)):
        if "0" <= s[i][j] and s[i][j] <= "9":
            temp_string = temp_string + s[i][j]
        elif s[i][j] == "+":
            temp_nums.append(int(temp_string))
            sum = 0
            for k in temp_nums:
                sum += k
            ans += sum
            temp_nums.clear()
            temp_string = ""
        elif s[i][j] == "*":
            temp_nums.append(int(temp_string))
            prod = 1
            for k in temp_nums:
                prod *= k
            ans += prod
            temp_nums.clear()
            temp_string = ""
    if temp_string: 
        temp_nums.append(int(temp_string))

print(ans)