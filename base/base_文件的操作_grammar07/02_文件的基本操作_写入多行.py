f = open('demo1.txt', mode='w', encoding='utf8')
# 多行写入，传入列表，

f.writelines(['今天\n', '明天\n', '后天\n'])
f.close()
