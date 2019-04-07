print("-----------------------------------------------------")
alien0 = {"color": "blue", "size": "12"}
print(alien0["color"])
print(alien0["size"])

print("-----------------------------------------------------")

alien0 = {"color": "blue", "size": "12"}
alien0["name"] = "yuan"
print(alien0)
print("-----------------------------------------------------")

alien0 = {"color": "blue", "size": "12"}
alien0["color"] = "red"
print(alien0)
print("-----------------------------------------------------")

alien0 = {"color": "blue", "size": "12"}
del alien0["color"]
print(alien0)

print("-----------------------------------------------------")
alien0 = {"color": "blue", "size": "12", "exe": "10"}
for key, val in alien0.items():
    print(key)
    print(val)

print("-----------------------------------------------------")
alien0 = {"color": "blue", "size": "12", "exe": "10"}
alien1 = {"color": "red", "size": "12", "exe": "10"}
alien2 = {"color": "yellow", "size": "12", "exe": "10"}

aliens = [alien0, alien1, alien2]
for alien in aliens:
    print(alien)

print("-----------------------------------------------------")
# 使用range()生产多个外星人
alien = []
for val in range(10):
    alien0 = {"color": "blue", "size": "12", "exe": "10"}
    alien.append(alien0)
for val in alien:
    print(val)

print("-----------------------------------------------------")
# 使用切片修改后5个外星人信息
for val in alien[-5:]:
    if val['color'] == 'blue':
        val['size'] = '15'
for val in alien:
    print(val)
print("-----------------------------------------------------")
favoriteLanguages = {
    "yuan": ["ruby", "java", "python"],
    "tuo": ["ruby", "php", "python"],
}

for key, val in favoriteLanguages.items():
    print(key + "最喜欢的语言是:")
    for v in val:
        print(v)
print("-----------------------------------------------------")
users = {
    "yuan": {
        "firstName": "yuan",
        "lastName": "tuo",
        "location": "sc"
    },

    "tuo": {
        "firstName": "tuo",
        "lastName": "yuan",
        "location": "cs"
    }
}
for key, val in users.items():
    fullName = val["firstName"] + val["lastName"]
    location = val["location"]
    print(fullName + " " + location)
print("-----------------------------------------------------")
