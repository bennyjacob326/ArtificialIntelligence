#search

import state
import frontier

def printIt(pushed, popped):
    print("average number pushed:", pushed)
    print("average number popped:", popped)


def search(n):
    popped = 0
    pushed = 0
    s=state.create(n)
    print(s)
    f=frontier.create(s)
    while not frontier.is_empty(f):
        s=frontier.remove(f)
        popped = popped + 1
        if state.is_target(s):
            printIt(pushed, popped)
            return [s, f[1]]
        ns=state.get_next(s)
        for i in ns:
            pushed = pushed + 1
            frontier.insert(f,i)
    return 0


print(search(4))







