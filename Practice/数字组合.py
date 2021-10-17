# 渣渣葡萄
# 开发时间：2021/10/17 17:10
total=0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != j)and(j != k)and(k != i):
                print(i,j,k)
                total+=1
print(total)
