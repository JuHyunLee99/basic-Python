# 복합형

# 리스트
arr = [1,2,3,4,5,6,7,8,9,10]
print(arr)

sum = 0
for i in arr:
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World', True]
print(arr3)
print(type(arr3))
print('arr1의 2번 인덱스값' + str(arr1[2]))

arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]]
print(arr6)

arr7 = [[1,2,3,4],5,6,7,8]
print(arr7)

# 튜플 : 리스트와 거의 같음
tuple1 = (1,2,3,4)
print(tuple1)
print(type(tuple1))
# 리스트는 요소의 추가, 수정, 삭제가 가능하지만,
arr5.append(4)
print(arr5)
# 튜플은 모두가 불가
# tuple1.append(4)
#print(tuple1)  # 오류

#딕셔너리
spiderman = {  'name' : 'Peter Parker',
                'age' : 18,
             'weapon' : 'Web Shooter'}
print(spiderman)
print(spiderman['weapon'])
print(type(spiderman))

#집합
set1 = set([1,2,3,4])
print(set1)

set2 = set("Hello World")
print(set2)     # 집합은 중복을 허용하지 않는다.     
# {'l', 'r', 'H', 'd', 'o', 'W', ' ', 'e'}