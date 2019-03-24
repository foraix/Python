# Python基础自学之路

## 变量和简单数据类型

#### 2.2变量

+ 添加变量将导致Python解释器需要更多工作
+ 在程序中可以随时修改变量的值，而Python始终记录变量的最新值

#### 2.2.1变量的命名和使用

+ 变量名只能包含字母，数字，下划线。
+ 可以以字母下划线打头，但不能用数字打头
+ 变量名中间不能有空格，可以使用下划线分割单词，如greeting_message
+ 不能将Python关键字和函数名作为变量名
+ 变量名应该简短同时具有描述性
+ 建议少用小写字母l和字母oO，因为任意被看成是数字

#### 2.2.2使用变量时避免命名错误

+ 很多编程都很简单，但却有不少优秀的成员因为变量名字这样的微小错误而而花费大量时间

#### 2.3字符串

+ 在Python中，用引号引起来的都时字符串，可以是单引号，也可以是双引号，如下也是合理的

```python
message = "'xxx','sss"
print(message)
```

#### 2.3.1使用方法修改字符串的大小写

```python
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
```

+ 存储数据时，lower()方法很有用，很多时候无法依靠用户提供正确的大小写，需要将字符串全部化为小写，再存储，需要显示时，将将其转为需要的大小写方式

#### 2.3.2合并字符串

```python
# 合并字符串
firstName = "yuan"
lastName = "tuo"
fullName = firstName + lastName
print(fullName)

# 上述操作的整合
message = "Hello " + fullName.title() + "!"
print(message)
```

#### 2.3.4删除空白

+ Python能够发现字符串中的空白，例如"Python" 和 "Python  " 是两个不同的字符串

```python
# rstrip() 可以去除尾部空白
message = " xxxx "
print(message.rstrip())

# lstrip() 可以去除首部空白
print(message.lstrip())

# strip() 可以去除两端空白
print(message.strip())
```

#### 2.4整数

+ 终端会话中，Python会直接返回运算结果
+ Python使用两个乘号表示乘方,不能使用多个表示多次方

```python
print(2 ** 9)

# 下面这种写法是错误的
# print(2 *** 9)
```

#### 2.4.2浮点数

+ Python将带小数点的数字都称之为浮点数

+ 有时候位数是不确定的

+ ```python
  # 会输出0.30000000000000004
  print(0.1 + 0.2)
  ```

#### 2.4.3使用str()避免类型转化错误

```python
age = 23
print("Hello My Love,Your age is " + str(age))
```

#### 2.6Python之禅

+ 尽可能的避繁就简
+ 代码需要优雅而漂亮
+ 选择简单的的解决方案
+ 编写有益的注释
+ 解决方案大家应该尽量一致
+ 不要企图编写完美无缺的代码，应该编写行之有效的代码，在做进一步改进

#### 第二章总结

> 2019年3月24日23:26:55
>
> ​	我觉得相较于java，c来说，Python的入门显然是更加容易的，但我相信简单有简单的好处，但必然也有很大的缺点存在，只是入门的我还无法体会，我坚信Python的理念好的是远远大于不好的，但是错误的终将主导Python的未来，希望路上有大佬不断的改进，延长Python的青年期。希望自己能坚持学完Python基础，加油，最后感谢自己的女朋友对自己心理上的指导！(*^__^*) 嘻嘻……

