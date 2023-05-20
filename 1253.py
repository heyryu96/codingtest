# N: 데이터 개수
# Result: 좋은 수 개수 저장 변수
# A: 수 데이터 저장 리스트
# A 리스트 정렬
N = int(input())
Result = 0
A = list(map(int, input().split()))
A.sort()

# find: 찾고자 하는 값
# 포인터 i, 포인터 j
for k in range(N):
    find = A[k]
    i = 0
    j = N - 1
    while i < j:  # 투 포인터 알고리즘
        if A[i] + A[j] == find: # find는 서로 다른 두 수의 합이어야 함을 체크
            if i != k and j != k:
                Result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
            elif A[i] + A[j] < find:  # 두 수의 합이 find 보다 작을 땐 시작 포인터를 크게
                i += 1
            else: # 두 수의 합이 find 보다 클 땐 종료 포인터를 작게
                j -= 1

print(Result)