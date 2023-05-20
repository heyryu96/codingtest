# N: 데이터 개수, L: 최솟값을 구하는 범위
# mydeque: 데이터를 담을 덱 자료구조
# now: 주어진 숫자 데이터를 가지는 리스트

from collections import deque

N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    # 아이디어1. 나보다 큰 데이터 삭제하기
    # mydeque에서 (값, 인덱스) 형태로 저장
    # 인덱스 -1: 뒤에서 첫 번째(가장 마지막) 요소

    # mydeque에 데이터가 있을 때 까지 & 제일 끝에 있는 값과 현재 리스트 값과 비교해서
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    
    # 덱의 마지막 위치에 현재 값 저장
    mydeque.append((now[i], i))

    # 아이디어2. 슬라이딩 윈도우 벗어난 데이터 삭제
    if mydeque[0][1] <= i-L:  # 윈도우 범위를 벗어나면
        mydeque.popleft() # 덱의 1번째 데이터 출력

    print(mydeque[0][0], end=' ')

print(mydeque)