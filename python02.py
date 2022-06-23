print("-" * 5, "튜플 사용하기", "-" * 5)

t1 = ()
t2 = (1,)
t3 = (1, 2, 3)
t4 = 1, 2, 3
t5 = ('a', 'b', ('ab', 'cd'))

print("t1 : {0}".format(t1))
print("t2 : {0}".format(t2))
print("t3 : {0}".format(t3))
print("t4 : {0}".format(t4))
print("t5 : {0}".format(t5))

print()

print("튜플 t2의 0 index : {0}".format(t2[0]))
# 튜플 t1은 빈 튜플이기 때문에 index가 없어서 접근이 불가능
# print("튜플 t1의 0 index : {0}".format(t1[0]))
# 튜플은 읽기 전용이기 때문에 수정이 불가능 함
# t1[0] = 1
# t2[0] = 1

# 튜플 생성 시 요소를 1개만 사용할 경우에도 ()를 생략할 수 있음
t6 = 1,
print("t6 : {0}".format(t6))

print("t3[:] : {0}".format(t3[:]))
print("t3[1:] : {0}".format(t3[1:]))
print("t3[:3] : {0}".format(t3[:3]))
print("t3[1:3] : {0}".format(t3[1:3]))


print()
print("튜플 t3의 길이 : {0}".format(len(t3)))

print()
t7 = (1, 2, 'a', 'b')
t8 = (3, 4)
print("튜플 t7 : {0}".format(t7))
print("튜플 t8 : {0}".format(t8))
print("튜플 t7 + t8 = {0}".format(t7 + t8))
t9 = t7 + t8
print("튜플 t7 + t8 = {0}".format(t9))
t9 = t8 * 3
print("튜플 t8 * 3 = {0}".format(t9))





