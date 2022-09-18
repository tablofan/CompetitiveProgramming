import os
import sys
from io import BytesIO, IOBase
from collections import defaultdict
def solve():
    s = input()
    a = "abcdefghijklmnopqrstuvwxyz"
    reva = a[::-1]
    d = defaultdict(list)
    for i,v in enumerate(s):
        d[v].append(i+1)
    # print(d)
    start = a.index(s[0])
    end = a.index(s[-1])
    cost = abs(start-end)
    jumps = 0
    res = []
    if start <= end:
        for i in a[start:end+1]:
            jumps += len(d[i])
            res += d[i]
    else:
        # print(reva[25-start:25-end+1])
        for i in reva[25-start:25-end+1]:
            jumps += len(d[i])
            res += d[i]
    print(f'{cost} {jumps}')
    print(*res)


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