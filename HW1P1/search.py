# search

import state
import frontier


def search(n):
    s = state.create(n)  # creates a random state
    f = frontier.create(s)  # diff based on search way
    while not frontier.is_empty(f):
        # count nums of removed
        s = frontier.remove(f)
        f[4] = f[4] + 1
        if state.is_target(s):
            # counter of f[1], div by amount of times run

            frontier.adder(f[4], f[5], f[1])
            return [s, f[1]]
        ns = state.get_next(s)
        # print(ns)
        for i in ns:
            # count nums of insert
            frontier.insert(f, i)
            f[5] = f[5] + 1
    return 0


for x in range(100):
    answer = search(3)

frontier.getAll()



