counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "runoob111"     # 字符串

print(counter)
print(miles)
print(name)
#Python允许你同时为多个变量赋值
a = b = c = 1
print(a)
print(b)
print(c)

# 两个整型对象 1 和 2 的分配给变量 a 和 b，字符串对象 "runoob" 分配给变量 c。
a, b, c = 1, 2, "runoob"
print(a)
print(b)
print(c)

a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
isinstance(a, int)
