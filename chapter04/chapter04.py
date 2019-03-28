cars = ["audi", "bmw", "benz"]
for car in cars:
    print(car)
    print(car.title() + " is very good")
print("test")

print("-------------------------------------------------")
# 这个语句看似会打印1到5,但实际上只会打印1到4
for val in range(1, 5):
    print(val)
print("-------------------------------------------------")

# 使用list()将数字转化为列表
list1 = list(range(1, 5))
print(list1.insert(0, 2))
print(list1)

# 2到15之间的偶数
evenNumbers = list(range(2, 15, 2))
print(evenNumbers)
print("-------------------------------------------------")

# 创建1到10的数平方的列表
squares = []
for val in range(1, 11):
    squares.append(val ** 2)
print(squares)
print("-------------------------------------------------")

squares = []
for val in range(1, 11):
    squares.append(val ** 2)
print(max(squares))
print(min(squares))
print(sum(squares))
print("-------------------------------------------------")

# 使用列表解析
squares = [val ** 2 for val in range(1, 15)]
print(squares)

squares = [val for val in range(1, 15, 3)]
print(squares)
print("-------------------------------------------------")

players = ["yuan", "han", "su", "wang"]
print(players[0:2])
# 全部打印
print(players[:])
# 打印倒数三个
print(players[-3:])

print("-------------------------------------------------")

# 遍历切片
for val in players[-2:]:
    print(val.title())
print("-------------------------------------------------")

# 复制列表 可以发现使用切片复制是两个不相干的实体，是一种完全复制
newPlayers = players[:]
print(newPlayers)
newPlayers.append("xxx")
print(players)
print(newPlayers)

# 可以发现通过变量名赋值，并非完全复制，两个变量名字指向的是同一个对象
print("-----")
newPlayers = players
newPlayers.append("xxx")
print(players)
print(newPlayers)

print("-------------------------------------------------")

