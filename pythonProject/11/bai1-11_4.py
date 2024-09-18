#bai1
def is_subset(A, B):
    return set(A).issubset(set(B))
T = int(input())
for i in range(T):
    print(i + 1)
    m, n = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    result = is_subset(A, B)
    print( result)
    print()



