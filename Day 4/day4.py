# [1518-03-05 23:57] Guard #2963 begins shift
# [1518-03-06 00:25] falls asleep
# [1518-03-06 00:46] wakes up
# [1518-03-07 00:01] Guard #89 begins shift
# [1518-03-07 00:15] falls asleep
# [1518-03-07 00:33] wakes up
from collections import defaultdict
lines = open("input.txt").read().split('\n')
lines.sort()

def parseTime(line):
    words = line.split()
    date, time = words[0][1:], words[1][:-1]
    return int(time.split(':')[1])

C = defaultdict(int)
CM = defaultdict(lambda:defaultdict(int))
guard = None
asleep = None
for line in lines:
    if line:
        time = parseTime(line)
        if 'begins shift' in line:
            guard = int(line.split()[3][1:])
            asleep = None
        elif 'falls asleep' in line:
            asleep = time
        elif 'wakes up' in line:
            for t in range(asleep, time):
                CM[guard][t]+=1
                C[guard] += 1

def argmax(d):
    best = None
    for k, v in d.items():
        if best is None or v > d[best]:
            best = k
    return best
best_guard = argmax(C)
best_min = argmax(CM[best_guard])

print (best_guard, best_min)
print (best_guard * best_min)