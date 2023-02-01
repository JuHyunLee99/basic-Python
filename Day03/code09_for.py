# for문

# for문은 리스트, 튜플 등과 만나면 강력한 능력

# ex1. 숫자
arr1 = [1,2,3,4,5]
sum = 0

for item in arr1:
    print(item)
    print(f'{item:2.2f}')

    sum += item

print('합계는', sum)

# ex2. 문자
arr2 =  ('me', 'my', 'friend', 'jane')

for item in  arr2:
    print(f'{item:>10}')    # 10칸 오른쪽 정렬

# ex3. range() 내장함수
vals = [i for i in range(1, 11)]    # 10까지이면 인덱스+1 해야함
print(vals)

# ex4. for문의 continue / 홀수만 출력하기
num = 0
for item in vals:
    num += 1
    if num % 2 ==0:
        continue    # 이후의 것을 수행하지 않고 다시 for무능로 감.
    else:
        print(num, '번 수는', item, '입니다')

# ex5. for문의 break문
num = 0
for item in vals:
    num += 1
    if num % 2 == 0:
        break
    else:
        print(f'{num}번 수는 {item}입니다')


