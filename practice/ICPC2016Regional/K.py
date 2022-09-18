from collections import Counter
c = Counter(input().upper())
aus = Counter("KANGAROO")
nz = Counter("KIWIBIRD")
a = 0
b = 0
for i in c:
    a += aus[i]*c[i]
    b += nz[i]*c[i]
if a>b:
    print("Kangaroos")
elif b>a:
    print("Kiwis")
else:
    print("Feud continues")