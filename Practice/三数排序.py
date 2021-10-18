# 渣渣葡萄
# 开发时间：2021/10/18 10:21
raw = []
for i in range(3):
    x = int(input('int%d: ' % (i)))
    raw.append(x)

for i in range(len(raw)):
    for j in range(i, len(raw)):
        if raw[i] > raw[j]:
            raw[i], raw[j] = raw[j], raw[i]
print(raw)

raw2 = []
for i in range(3):
    x = int(input(f'int{i:d}: '))
    raw2.append(x)
print(sorted(raw2))

raw3 = []
x=int(input("x"))
y=int(input("y"))
z=int(input("z"))
print(sorted(raw3))

