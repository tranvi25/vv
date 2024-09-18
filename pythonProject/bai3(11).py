def INTERSEC(A, B):
    return sorted(list(A.intersection(B)))
T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))
    result = INTERSEC(A, B)
    if result:
        print(result)
    else:
        print("NULL")
