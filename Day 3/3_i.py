def findmax(s):
    max = int(s[0])
    pos = 0
    for i in range(len(s)):
        if int(s[i]) > max:
            max = int(s[i])
            pos = i
    return max,pos

sum = 0

with open("Day 3/in.txt", "r") as file:
    for line in file:
        l = line.replace("\n","")
        max, pos = findmax(l)

        if pos == len(l)-1:
            max1,pos1 = findmax(l[:-1])
            max2 = max
        else:
            max1 = max
            max2,pos2 = findmax(l[pos+1:])
        
        sum += max1 * 10 + max2

print(sum)
        