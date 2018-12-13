c2 = 0
c3 = 0
ids = []
#Part 1
for line in open("input.txt"):
    s = line.strip()
    ids.append(s)
    count = {}
    for c in s:
        if c not in count:
            count[c] = 0
        count[c] +=1
    has_two = False
    has_three = False
    for k,v in count.items():
        if v== 2:
            has_two = True
        if v==3:
            has_three = True
    if has_two:
        c2+=1
    if has_three:
        c3+=1
print (c2 *c3)

#Part 2
for x in ids:
    for y in ids:
        diff = 0
        for i in range(len(x)):
            if x[i] != y[i]:
                diff += 1
        if diff == 1:
            ans = []
            for i in range(len(x)):
                if x[i] == y[i]:
                    ans.append(x[i])
            print (''.join(ans))
