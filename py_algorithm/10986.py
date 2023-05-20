import sys
input = sys.stdin.readline

# n: 수열의 개수
# m: 나누어 떨어져야 하는 수
n, m = map(int, input().split())

# A: 원본 수열 저장 리스트
# S: 합 배열
# C: 같은 나머지의 인덱스를 카운트하는 리스트
# answer: 정답 변수
A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i]  #합 배열 저장

for i in range(n):
    remainder = S[i] % m  # 합 배열을 M으로 나눈 나머지 값
    if(remainder == 0):
        answer += 1
    C[remainder] += 1 # 같은 나머지 인덱스 값 증가

for i in range(m):
    if C[i] > 1:  # 같은 나머지 인덱스가 2개 이상이면
        answer += ((C[i] * (C[i] - 1)) // 2)  # 조합(순서 상관 없이 n개 중 r개 뽑는) 계산 후 결과 값에 더해줌
        # C[i]개 중 2개를 뽑는 경우의 수: C[i] * C[i]-1 / 2

print(answer)