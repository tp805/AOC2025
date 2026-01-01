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
        flag = [0 for _ in range(len(l))]
        flag[pos] = 1
        currans = str(max)

        for _ in range(11):
            curr_point = 0
            max = ""
            pos = 0

            for i in range(len(l)):
                if flag[i] == 1:
                    curr_point += 1
                    continue
                test = currans[0:curr_point] + l[i] + currans[curr_point:]
                if len(test)>len(max) or (len(test)==len(max) and test>max):
                    max = test
                    pos = i
            
            flag[pos] = 1
            currans = max
        
        sum += int(currans)

print(sum)
        