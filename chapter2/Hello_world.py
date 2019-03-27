message = "Hello Python"
print(message)

message = "'xxx','sss"
print(message)

# 将字符串首字母大写
title = "title"
title = title.title()
print(title)

# 将字符串全部大写
title1 = title.upper()
print(title1)

# 将字符串全部小写
title2 = title1.lower()
print(title2)

# 合并字符串
firstName = "yuan"
lastName = "tuo"
fullName = firstName + lastName
print(fullName)

# 上述操作的整合
message = "Hello " + fullName.title() + "!"
print(message)

# rstrip() 可以去除尾部空白
message = " xxxx "
print(message.rstrip())

# lstrip() 可以去除首部空白
print(message.lstrip())

# strip() 可以去除两端空白
print(message.strip())