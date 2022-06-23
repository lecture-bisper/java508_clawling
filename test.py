print("파이썬 시작해보기.")

print(" 큰따옴표3개 사용")

a = "문자열을 여러 라인 입력할 경우" \
    "이런 식으로 입력해야" \
    "합니다."

b = "문자열을 여러 라인 입력할 경우\n" \
    "이런 식으로 입력해야\n" \
    "합니다."

c = """문자열을 여러 라인 입력할 경우
이런 식으로 입력해야
합니다."""

print(a)
print(b)
print(c)


print("-" * 5, "문자열 슬라이싱", "-" * 5)

str = "파이썬의 문자열 슬라이싱 사용해보기"

print("원본 문자열 : {0}".format(str))
print("str[5:13] : {0}".format(str[5:13]))
print("str[:13] : {0}".format(str[:13]))
print("str[5:] : {0}".format(str[5:]))
print("str[:] : {0}".format(str[:]))


print("-" * 5, "문자열 포매팅", "-" * 5)

print("파이썬의 {0} 포매팅 사용해보기".format("문자열"))
print("{0}의 {1} {2} 사용해보기".format("파이썬", "문자열", "포매팅"))

print("-" * 5, "문자열 함수 사용하기", "-" * 5)

str1 = "문자열 함수를 사용해 봅시다"
str2 = "Python is the best choice"

print("문자열의 길이 : {0}".format(len(str1)))

print("변수 str2에 o의 개수는 : {0}".format(str2.count("o")))

# find() : 지정한 단어가 검색되면 해당 위치를 출력하고 없으면 -1을 출력
print("변수 str1에 단어 '함수'의 위치는 : {0}".format(str1.find("함수")))

# index() : 지정한 단어가 검색되면 해당 위치를 출력하고 없으면 에러 발생
# 예외처리가 필요함
print("변수 str1에 단어 '함수'의 위치는 : {0}".format(str1.index("함수")))

str3 = "abcd"
print("원본 변수 str3 : {0}".format(str3))
str3 = ",".join(str3)
print("수정된 변수 str3 : {0}".format(str3))

str4 = "       빈 문자열 제거하기         "
print("원본 문자열 : {0}".format(str4))
print("왼쪽 공백 제거 : {0}".format(str4.lstrip()))
print("오른쪽 공백 제거 : {0}".format(str4.rstrip()))
print("양쪽 공백 모두 제거 : {0}".format(str4.strip()))

str5 = "Life is too short"
print("원본 문자열 : {0}".format(str5))
print("수정된 문자열 : {0}".format(str5.replace("Life", "Leg")))

print(str5)
print(str5.split(" "))




