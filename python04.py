print("-" * 5, "집합 사용하기", "-" * 5)

s1 = set([1, 2, 3, 3, 2, 1, 5, 6, 7, 8, 9, 0, 7, 8, 6])
print(s1)

s2 = set("hello")
print(s2)

for item in s2:
    print(item)

list_s2 = list(s2)
print(list_s2)
print(list_s2[0])
print(list_s2[1:3])
print(list_s2[1:])
print(list_s2[:2])
print(list_s2[:])


print("-" * 5, "set을 이용한 교집합, 합집합, 차집합", "-" * 5)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

intersection = s1 & s2
print("집합 s1 & s2 = {0}".format(intersection))

union = s1 | s2
print("집합 s1 | s2 = {0}".format(union))

difference = s1 - s2
print("집합 s1 - s2 = {0}".format(difference))
difference = s2 - s1
print("집합 s2 - s1 = {0}".format(difference))

print()
print("원본 집합 s1 : {0}".format(s1))
s1.add(7)
s1.add(8)
print("add 후 집합 s1 : {0}".format(s1))

s1.remove(1)
s1.remove(2)
s1.remove(3)
print("remove 후 집합 s1 : {0}".format(s1))

s1.update([1, 2, 3, 9])
print("update 후 집합 s1 : {0}".format(s1))


print()

a, b = ("python", "life")
print(a)
print(b)

(c, d) = "python", "life"
print(c)
print(d)

[e, f] = ["python", "life"]
print(e)
print(f)




print(a)
print(b)
a, b = b, a
print(a)
print(b)

