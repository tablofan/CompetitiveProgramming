import sys
def main():
    i = 1
    while True:
        print(f'? {i} {i+1}')
        sys.stdout.flush()
        res1 = int(input())
        if res1 == -1:
            print(f'! {i}')
            break
        print(f'? {i+1} {i}')
        sys.stdout.flush()
        res2 = int(input())
        if res2 != res1:
            print(f'! {res1+res2}')
            break
        i += 1