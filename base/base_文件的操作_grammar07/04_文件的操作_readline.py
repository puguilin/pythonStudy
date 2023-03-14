f = open('demo1.txt', mode='r', encoding='utf8')
# print(f.readline())
while True:
    content = f.readline()
    if not content:
        break
    print(content)
# 一行一行读取