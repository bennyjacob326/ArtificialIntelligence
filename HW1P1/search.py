# search

import state
import frontier


def search(n):
    s = state.create(n)  # creates a random state
    f = frontier.create(s)  # diff based on search way
    while not frontier.is_empty(f):
        s = frontier.remove(f)
        f[4] = f[4] + 1
        if state.is_target(s):
            print("depth of this one is ", f[1])
            frontier.adder(f[4], f[5], f[1])
            return [s, f[1]]
        ns = state.get_next(s)
        # print(ns)
        for i in ns:
            frontier.insert(f, i)
            f[5] = f[5] + 1
    return 0


for x in range(100):
    answer = search(3)

frontier.getAll()



# search(2):
# average depth: 1.74
# average number pushed: 7.1
# average number popped: 6.51
#
# search(3):
# average depth: 6.04
# average number pushed: 1177.26
# average number popped: 678.3
#
# search(4) took wayyy too long to test

