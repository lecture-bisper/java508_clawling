print("-" * 5, "리스트 사용하기", "-" * 5)

a = [1, 2, 3, 4, 5]

print("원본 리스트 : {0}".format(a))

print("리스트 슬라이싱 a[0:2] : {0}".format(a[0:2]))
print("리스트 슬라이싱 a[:2] : {0}".format(a[:2]))
print("리스트 슬라이싱 a[3:] : {0}".format(a[3:]))
print("리스트 슬라이싱 a[1:4] : {0}".format(a[1:4]))
print("리스트 슬라이싱 a[:] : {0}".format(a[:]))

print("-" * 5, "리스트 연산하기", "-" * 5)

b = [1, 2, 3]
c = [4, 5]

print("원본 리스트 b : {0}\n원본 리스트 c : {1}".format(b, c))
print("리스트 b + c = {0}".format(b + c))
print("리스트 b * 3 = {0}".format(b * 3))

print("-" * 5,"리스트 함수 사용하기", "-" * 5)

list_a = [1, 2, 3, 4, 5, 6, 7]

print("리스트 길이 : {0}".format(len(list_a)))

print("원본 리스트 list_a : {0}".format(list_a))
del list_a[3]
print("삭제 후 리스트 list_a : {0}".format(list_a))

list_a.remove(3)
list_a.remove(5)
print("remove 사용 후 list_a : {0}".format(list_a))

list_a.pop()
print("pop 사용 후 list_a : {0}".format(list_a))
list_a.pop(1)
print("pop을 사용하여 지정한 index의 데이터 삭제 : {0}".format(list_a))


print()
print("원본 리스트 list_a : {0}".format(list_a))

list_a.append(8)
list_a.append(9)
print("append 사용 후 list_a : {0}".format(list_a))

list_a.insert(1, 2)
list_a.insert(2, 3)
print("insert 사용 후 list_a : {0}".format(list_a))


print()

list_b = [4, 7, 2, 9, 1]
print("원본 리스트 list_b : {0}".format(list_b))

list_b.sort()
print("sort 사용 후 list_b : {0}".format(list_b))

# reverse() 는 단순히 현재 리스트의 요소 위치를 반대로 변경하기만 함
# 역순 정렬이 아님, 역순 정렬 시 sort() 사용 후 reverse() 사용
list_b.reverse()
print("reverse 사용 후 list_b : {0}".format(list_b))

print()

print("index 를 사용하여 4의 위치 찾기 : {0}".format(list_b.index(4)))
print("count를 사용하여 7의 개수 구하기 : {0}".format(list_b.count(7)))







