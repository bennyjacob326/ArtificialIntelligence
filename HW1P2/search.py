# search

import state
import frontier

popped = 0
pushed = 0
depth = 0


def printIt():
    global popped
    global depth
    global pushed
    print("average depth: ", depth / 100)
    print("average number pushed:", pushed / 100)
    print("average number popped:", popped / 100)


def search(n):
    global popped
    global depth
    global pushed
    s = state.create(n)
    f = frontier.create(s)
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        popped = popped + 1
        if state.is_target(s):
            if len(f[0]) != 0:
                depth = depth + len(s[1])
            return [s, f[1]]
        ns = state.get_next(s)
        for i in ns:
            pushed = pushed + 1
            frontier.insert(f, i)
    return 0


for x in range(100):
    search(4)
printIt()

# hdistance1
# average depth:  15.96
# average number pushed: 75223.18
# average number popped: 36213.89

# hdistance2
# average depth:  15.92
# average number pushed: 2220.47
# average number popped: 1105.24
#
#
# 2*hdistance1
# average depth:  15.86
# average number pushed: 13070.73
# average number popped: 6058.36

# 2*hdistance2
# average depth:  16.43
# average number pushed: 1001.09
# average number popped: 498.38

# observations:
# while the runtime is reduced significantly by using a weighted A* search,
# the optimality of the solution did not change much
