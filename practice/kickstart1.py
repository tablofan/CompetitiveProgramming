
#Sample Problem
# for t in range(int(input())):
#     m = int(input().split()[1])
#     s = sum(list(map(int,input().split())))
#     print("Case #"+ str(t+1) + ": " + str(s%m))


#Centauri Prime
# def get_ruler(kingdom):
#     vowel = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
#     if kingdom[-1] in vowel:
#         return 'Alice'
#     if kingdom[-1] == 'y' or kingdom[-1] == 'Y':
#         return 'nobody'
#     return 'Bob'
#
# def main():
#     for t in range(int(input())):
#         kingdom = input()
#         print('Case #%d: %s is ruled by %s.' % (t + 1, kingdom, get_ruler(kingdom)))
#
# if __name__ == '__main__':
#     main()


#H-Index
def h_index(n, citations):
    ans = []
    # TODO: Complete the function to get the H-Index scores after each paper
    for i,v in enumerate(citations):

    return ans


if __name__ == '__main__':
    t = int(input())

    for test_case in range(1, t + 1):
        n = int(input())                      # The number of papers
        citations = map(int, input().split()) # The number of citations for each paper
        h_index_scores = h_index(n, citations)
        print("Case #" + str(test_case) + ": " + ' '.join(map(str, h_index_scores)))

#Hex

#Milk Tea