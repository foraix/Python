print("--------------------------------------------")
message = input("Tell me your name!")
print("Hello:" + message)
print("--------------------------------------------")
# 未验证的用户信息
unconfirmedUsers = ["alice", "mike", "yuan"]
# 已经验证的用户信息
confirmedUsers = []

# 一直验证，直到该列表为空时
while unconfirmedUsers:
    # 获得当前验证的用户信息
    currentUser = unconfirmedUsers.pop()
    # 打印正在验证信息
    print("Verifying user is " + currentUser.title())
    confirmedUsers.append(currentUser)

print("\nThe following users has been confirmed:")

# 显示已经验证的人的信息
for val in confirmedUsers:
    print(val)

print("--------------------------------------------")
pets = ["cat", "cat", "dog", "pig"]
while "cat" in pets:
    pets.remove("cat")
print(pets)
print("--------------------------------------------")
