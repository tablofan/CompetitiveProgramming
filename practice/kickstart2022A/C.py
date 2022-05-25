def dfs(i, s):
    global res
    # print(f'{i = }')
    # print(f'{s = }')
    # print(f'{res = }')
    if i>5:
        pali6 = s[i - 6:i]
        pali6r = pali6[::-1]
        # print(f'{pali6 = }  {pali6r = }')
        if pali6 == pali6r:
            return
    if i>4:
        pali5 = s[i - 5:i]
        pali5r = pali5[::-1]
        # print(f'{pali5 = }  {pali5r = }')
        if pali5 == pali5r:
            return
    if i==len(s):
        res = "POSSIBLE"
        return
    if s[i] == '?':
        dfs(i+1, s[:i]+'0'+s[i+1:])
        dfs(i + 1, s[:i] + '1' + s[i + 1:])
        return
    return dfs(i+1,s)


def solve():
    global res
    res = "IMPOSSIBLE"
    n = int(input())
    s = input()
    dfs(0, s)
    return


def main():
    for i in range(int(input())):
        solve()
        print(f'Case #{i+1}: {res}')

if __name__=="__main__":
    res = "IMPOSSIBLE"
    main()