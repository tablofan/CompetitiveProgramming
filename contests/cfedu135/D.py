#!/usr/bin/env python
import os
import sys
from io import BytesIO, IOBase
import heapq

def solve():
    s = input()
    n = len(s)
    dp = [[1] * n for _ in range(n)]
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            dp[i][i + 1] = 2
    for k in range(4, n + 1, 2):
        for i in range(n):
            if i + k - 1 < n:
                x = 2
                if dp[i + 2][i + k - 1] == 2:
                    pass
                elif dp[i + 2][i + k - 1] == 1:
                    if s[i] == s[i + 1]:
                        x = min(x, 1)
                    elif s[i] > s[i + 1]:
                        x = min(x, 0)
                    else:
                        x = min(x, 2)
                else:
                    x = min(x, 0)
                if dp[i + 1][i + k - 1 - 1] == 2:
                    pass
                elif dp[i + 1][i + k - 1 - 1] == 1:
                    if s[i] == s[i + k - 1]:
                        x = min(x, 1)
                    elif s[i] > s[i + k - 1]:
                        x = min(x, 0)
                    else:
                        x = min(x, 2)
                else:
                    x = min(x, 0)
                y = 2
                if dp[i + 1][i + k - 1 - 1] == 2:
                    pass
                elif dp[i + 1][i + k - 1 - 1] == 1:
                    if s[i] == s[i + k - 1]:
                        y = min(y, 1)
                    elif s[i] < s[i + k - 1]:
                        y = min(y, 0)
                    else:
                        y = min(y, 2)
                else:
                    y = min(y, 0)
                if dp[i][i + k - 1 - 2] == 2:
                    pass
                elif dp[i][i + k - 1 - 2] == 1:
                    if s[i + k - 1] == s[i + k - 1 - 1]:
                        y = min(y, 1)
                    elif s[i + k - 1] > s[i + k - 1 - 1]:
                        y = min(y, 0)
                    else:
                        y = min(y, 2)
                else:
                    y = min(y, 0)
                dp[i][i + k - 1] = max(x, y)
    ans = dp[0][-1]
    if ans == 0:
        print('Bob')
    elif ans == 1:
        print('Draw')
    else:
        print('Alice')



def main():
    for _ in range(int(input())):
        solve()

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
