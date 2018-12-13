import itertools
#Part 1
input = [int(x) for x in open("input.txt").readlines()]
print(sum(input))

#Part 2
freq = 0
seen = {0}

for num in itertools.cycle(input):
    freq += num
    if freq in seen:
        print(freq); break
    seen.add(freq)