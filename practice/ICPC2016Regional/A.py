a,b = map(int,input().split())


def ring(a):
    return int((-1+(a-1)**0.5)//2)


def excess(a,ring):
    return a-4*(ring*(ring+1))-2


ra = ring(a)
rb = ring(b)
ea = excess(a,ra)
eb = excess(b,rb)

def pos(e,ring):
    p = [-ring,-ring-1]
    if e>(ring*2+1):
        p[0]+=ring*2+1
        e -= (ring*2+1)
    else:
        p[0]+=e
        return p
    if e>(ring*2+2):
        p[1]+=ring*2+2
        e -= (ring*2+2)
    else:
        p[1]+=e
        return p
    if e>(ring*2+2):
        p[0]-=(ring*2+2)
        e -= (ring*2+2)
        p[1]-=e
        return p
    else:
        p[0]-=e
        return p

pa = pos(ea,ra)
pb = pos(eb,rb)
print(abs(pa[0]-pb[0])+abs(pa[1]-pb[1]))
print(f'ra: {ra} rb: {rb}')
print(f'ea: {ea} eb: {eb}')
print(f'pa: {pa} pb: {pb}')