# file = open('text.txt',mode="w",encoding='utf-8')
# for i in range(3):
#     file.write('привет,мир')
#     file.write('привет,света')
# file.close()

import os
if 'ussr' not in os.listdir():#если папки нет в списке папок
    os.mkdir('ussr')#то создать папку

# for i in range(3):
#     file = open(f'file{i}.txt',mode="w",encoding='utf-8')
#     file.write('привет,мир')
#     file.write('привет,света')
# file.close()
file = open('file0.txt',mode="r",encoding='utf-8')
data = file.read()
file.close()
print(data)

for i in range (len(data)):
    if i == 0:
        data(i) = 1
    data[i]
    data[i] = int (data(i))
print(data)