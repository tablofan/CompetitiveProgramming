# B
# Maths
import math
def solve(a, b, c, d):
    f = ((3.0 * c / a) - ((b ** 2.0) / (a ** 2.0))) / 3.0
    g = (((2.0 * (b ** 3.0)) / (a ** 3.0)) - ((9.0 * b * c) / (a ** 2.0)) + (27.0 * d / a)) / 27.0
    h = ((g ** 2.0) / 4.0 + (f ** 3.0) / 27.0)
    if h > 0:
        R = -(g / 2.0) + math.sqrt(h)
        if R >= 0:
            S = R ** (1 / 3.0)
        else:
            S = (-R) ** (1 / 3.0) * -1
        T = -(g / 2.0) - math.sqrt(h)
        if T >= 0:
            U = (T ** (1 / 3.0))
        else:
            U = ((-T) ** (1 / 3.0)) * -1
        return (S + U) - (b / (3.0 * a))
    return "error"

n,T,v,d = map(int,input().split())
theta = 0
x,y,s = map(float,input().split())
z = s*(abs((1 - x**2 - y**2))**(1/2))
for _ in range(n-1):
    tx, ty, ts = map(float,input().split())
    tz = ts*(abs((1 - tx**2 - ty**2))**(1/2))
    theta += math.acos(tx*x+ty*y+tz*z)
    x,y,z = tx,ty,tz
if theta == 0:
    print(0.0)
else:
    x = (d/theta)**3
    t = solve(x,-3*x*T,3*x*T*T+(3/(4*math.pi))*v,1-x*T*T*T)
    r = (1+(3/(4*math.pi))*v*t)**(1/3)
    print(r*theta)

# Binary Search
# import math
# n,T,v,d = map(int,input().split())
# theta = 0
# x,y,s = map(float,input().split())
# z = s*(abs((1 - x**2 - y**2))**(1/2))
# for _ in range(n-1):
#     tx, ty, ts = map(float,input().split())
#     tz = ts*(abs((1 - tx**2 - ty**2))**(1/2))
#     theta += math.acos(tx*x+ty*y+tz*z)
#     x,y,z = tx,ty,tz
# c1 = theta/d
# c2 = (3*v)/(4*math.pi)
#
# def b(l,r,t):
#     res = ((1+c2*t)**(1/3))*c1+t
#     if res < T+0.000000001 and res>T-0.000000001:
#         return t
#     if res>T:
#         return b(l,t,(l+t)/2)
#     return b(t,r,(r+t)/2)
#
# res = b(0,T,T/2)
# print(((1+c2*res)**(1/3))*theta)