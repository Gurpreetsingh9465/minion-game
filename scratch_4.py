def minion_game(string):
    s = 0
    k = 0
    n = len(string)
    for i in range(n):
        if string[i] in ('A', 'E', 'I', 'O', 'U'):
            k += n - i # algorithm for sub string
        else:
            s += n - i
    if k == s:
        print("Draw")
    elif k > s:
        print("Kevin", k)
    elif s > k:
        print("Stuart", s)
if __name__ == '__main__':
    s = input()
    minion_game(s)