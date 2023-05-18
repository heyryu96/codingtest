# N: 재료의 개수
# M: 갑옷이 되는 번호
# A: 재료 데이터 저장 리스트
N = int(input())
M = int(input())
A = list(map(int, input().split()))

# A 리스트 정렬
A.sort()

# i: 시작 인덱스
# j: 종료 인덱스
# count: 정답 값
i = 0
j = N - 1
count = 0

while i < j:  # 투 포인터 이동 원칙에 따라 포인터를 이동하며 처리
    if A[i] + A[j] < M:
        i += 1  # 작은 번호 인덱스++
    elif A[i] + A[j] > M:
        j -= 1  #큰 번호 인덱스--
    else:
        count += 1
        i += 1
        j -= 1

print(count)