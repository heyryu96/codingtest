import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

# n:노드 개수, m:에지 개수
# A: 그래프 데이터 저장 인접 리스트
# visited 방문 기록 리스트
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

# DFS 구현
# visited 리스트에 현재 노드 방문 기록
# 현재 노드의 연결 노드 중 방문하지 않은 노드로 DFS 실행(재귀 함수 형태)
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# for m의 개수만큼 반복:
# A 인접 리스트에 그래프 데이터 저장
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

# for n의 개수만큼 반복
# if 방문하지 않은 노드가 있으면:
# 연결 요소 개수 값 1 증가
# DFS 실행
for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)
# 연결 요소 개수 값 출력
print(count)
print(A)
print(visited)