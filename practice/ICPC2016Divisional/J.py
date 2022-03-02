#J
n = int(input())
x = ["a","b"]
print(f"1 2 {x[n%2]}")
for i in range(3,n+1):
    print(" ".join([x[(n-i+1)%2], str(i),x[(n-i)%2]]))