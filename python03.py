print("-" * 5, "딕셔너리 사용하기", "-" * 5)

dic = {"name": "pey", "phone": "01012345678", "birth": "0623"}

print("원본 딕셔너리 dic : {0}".format(dic))
print("name : {0}\nphone : {1}\nbirth : {2}".format(dic["name"], dic["phone"], dic["birth"]))

print()
dic["email"] = "pey@test.co.kr"
print("데이터가 추가된 딕셔너리 : {0}".format(dic))
del dic["birth"]
print("데이터가 삭제된 딕셔너리 : {0}".format(dic))

print()

car_info = {"name": "토레스", "type": "SUV", "cc": "1497", "price": "2690", "color": "회색"}

keys = car_info.keys()
print("딕셔너리 car_info의 keys : {0}".format(keys))

# list() 를 사용하면 리스트 타입으로 데이터를 변환
list_keys = list(keys)
print(list_keys)
print(list_keys[0])
print(list_keys[1:4])

# 파이썬의 for문은 js의 for ~ in문 및 java의 향상된 for 문과 동일함
for item in keys:
    # 파이썬의 print문은 기본적으로 \n이 추가되어 있기 때문에 한 라인에 계속 데이터를 출력하려면 2번째 매개변수에 end='' 형태를 추가해야 함
    print(item, end=" ")


print()
values = car_info.values()
print("딕셔너리 car_info의 values : {0}".format(values))

list_values = list(values)
print("리스트로 변환된 values : {0}".format(list_values))
print(list_values[3])
print(list_values[1:3])
print(list_values[:3])
print(list_values[1:])
print(list_values[:])

for item in values:
    print(item, end=" ")


print()
items = car_info.items()
print("딕셔너링 car_info의 items : {0}".format(items))

for item in items:
    print("item : {0}, item[0] : {1}, item[1] : {2}".format(item, item[0], item[1]))


list_items = list(items)
print("리스트로 변환된 items : {0}".format(list_items))

print()
print("원본 딕셔너리 car_info : {0}".format(car_info))
car_info.clear()
print("clear 후 car_info : {0}".format(car_info))

car_info = {"name": "토레스", "type": "SUV", "cc": "1497", "price": "2690", "color": "회색"}

print("딕셔너리 car_info에 key 이름이 size 인 것이 있는가? {0}".format("size" in car_info))
print("딕셔너리 car_info에 key 이름이 name 인 것이 있는가? {0}".format("name" in car_info))

print()

print("딕셔너리 car_info : {0}".format(car_info))
print("car_info['name'] : {0}".format(car_info["name"]))
print("car_info.get('name') : {0}".format(car_info.get("name")))

print("car_info.get('size') : {0}".format(car_info.get("size")))
print("car_info['size'] : {0}".format(car_info["size"]))







