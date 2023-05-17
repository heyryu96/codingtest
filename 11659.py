# input()과 readline()은 기능상 큰 차이는 없지만, 속도 차이가 크다.
# input을 readline의 속도로 사용하려면 아래 두 줄을 추가하면 된다.
import sys
input = sys.stdin.readline

# 값 두 개를 입력받아 변수에 각각 저장 (띄어쓰기 구분)
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

# for 저장한 숫자데이터 차례대로 탐색
# numbers list 값을 기반으로 반복문 실행
for i in numbers:
    temp += i
    prefix_sum.append(temp) # 합 배열 만들기
    
# print(prefix_sum) # [0, 5, 9, 12, 14, 15]

# for 질의 개수만큼 반복:
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e]-prefix_sum[s-1])