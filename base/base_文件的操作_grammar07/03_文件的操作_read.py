f = open('demo1.txt', mode='r', encoding='utf8')
# f.read()
# 读取文件，读取全部文件
print(f.readlines())
print(f.read())
# 读取文件的时候，如果找不到文件，就会显示找不到文件的错误
# f.read(size)
print(f.read(5))
# size指的字符数，5个一组输出结果
# 文本模式，加size
f = open('demo1.txt', mode='rb')
# 以二进制的方法读取文件内容
content = f.read()
print(content)
