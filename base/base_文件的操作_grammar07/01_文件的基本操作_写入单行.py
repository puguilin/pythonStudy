# 如果文件存在，就打开，如果文件不存在，就新建文件
# open打开文件返回一个文件句柄
f = open('demo.txt', 'r', encoding='utf8')
# f.write('这是Python对文件的操作')
# 关闭当前操作
print(f.read(2))
f.close()
# 关键字w是覆盖