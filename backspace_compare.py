def sol1(S: str, T: str) -> bool:
    lS = len(S)
    lT = len(T)
    n = max(lS, lT)
    s = []
    t = []

    for i in range(n):
        if i < lS:
            if S[i] == '#' and len(s) >= 1:
                s.pop()
            if S[i] != '#':
                s.append(S[i])
        if i < lT:
            if T[i] == '#' and len(t) >= 1:
                t.pop()
            if T[i] != '#':
                t.append(T[i])

    return s == t


def sol2(S: str, T: str) -> bool:
    lastAcceptedS = len(S) - 1
    lastAcceptedT = len(T) - 1

    while lastAcceptedS >= 0 or lastAcceptedT >= 0:
        consecutiveBackS = 0
        while lastAcceptedS >= 0 and (consecutiveBackS > 0 or S[lastAcceptedS] == '#'):

            if S[lastAcceptedS] == '#':
                consecutiveBackS += 1
            else:
                consecutiveBackS -= 1

            lastAcceptedS -= 1

        consecutiveBackT = 0
        while lastAcceptedT >= 0 and (consecutiveBackT > 0 or T[lastAcceptedT] == '#'):

            if T[lastAcceptedT] == '#':
                consecutiveBackT += 1
            else:
                consecutiveBackT -= 1

            lastAcceptedT -= 1

        if lastAcceptedS >= 0 and lastAcceptedT >= 0:
            if S[lastAcceptedS] == T[lastAcceptedT]:
                lastAcceptedS -= 1
                lastAcceptedT -= 1
            else:
                return False
        elif lastAcceptedS >= 0 or lastAcceptedT >= 0:
            return False

    return lastAcceptedS < 0 and lastAcceptedT < 0


def backspaceCompare(S: str, T: str) -> bool:
    return sol2(S, T)


if __name__ == '__main__':
    # S = "ab#c"
    # T = "ad#c"
    # print(backspaceCompare(S, T))
    #
    # S = "ab#"
    # T = "a##a"
    # print(backspaceCompare(S, T))
    #
    # S = "ab##"
    # T = "c#d#"
    # print(backspaceCompare(S, T))
    #
    # S = "a##c"
    # T = "#a#c"
    # print(backspaceCompare(S, T))
    #
    # S = "a#c"
    # T = "b"
    # print(backspaceCompare(S, T))

    S = "j##yc##bs#srqpfzantto###########i#mwb"
    T = "j##yc##bs#srqpf#zantto###########i#mwb"
    print(backspaceCompare(S, T))
