import sys
input = sys.stdin.readline

# n: 리스트 크기, m: 질의 수
# A: 원본 리스트, D: 합 배열
n,m = map(int, input().split())

# 0으로 구성된 n+1만큼의 길이의 배열 선언
# [[0] * n] * n 으로 리스트를 초기화할 경우, n개의 [0] * n은 모두 같은 객체로 인식
# 다차원 리스트를 선언할 때,
# [[0 for j in range(n)] for i in range(n)]
# [[0] * n for i in range(n)] 로 선언하기
A = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

"""
리스트 내포함수를 이용하여 리스트 내부에서 인풋을 모두 받아버린다.

- input()을 받고 공백을 기준으로 split하여 ["1 2 3 4"] -> ["1", "2", "3", "4"]
- 나온 x를 int(x) 로 변환해준다. [1,2,3,4]
- 이때 각 리스트에 값 순서대로 a, b, c, d에 들어가게 된다. [a = 1, b = 2, c = 3, d = 4]
"""
for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        # 합 배열 구하기
        D[i][j] = D[i][j-1]+D[i-1][j]-D[i-1][j-1]+A[i][j]

for _ in range(m):
    for i in range(n+2):
      for j in range(n+1):
        print(A[i][j])
        if(j==n):
           print("\n")
    x1, y1, x2, y2 = map(int, input().split())
    # 구간 합 배열로 질의에 답변
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
