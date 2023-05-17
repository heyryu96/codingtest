# n: 입력된 자연수
n = int(input())

# 사용 변수 초기화
# count: 결과 변수
# start_index / end_index: 시작/종료 인덱스
# sum: 자연수의 합
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count+=1
        end_index+=1
        sum = sum+end_index
    elif sum > n:
        sum = sum - start_index
        start_index+=1
    else:
        end_index+=1
        sum=sum+end_index

print(count)