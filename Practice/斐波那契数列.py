# 渣渣葡萄
# 开发时间：2021/10/18 10:47
# 生成斐波那契数列
List = [0]
a, b = 0, 1
for i in range(20):
    a, b = b, a + b
    List.append(a)  # 往列表末尾添加一个元素
print(List)

"""2利用类和对象的方式"""


class Fib(object):
    def __init__(self):  # 除self以外的参数是传入参数
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a  # 每次调用__next__()都返回一个值，这个值大于100000时，停止迭代，退出循环


for n in Fib():
    print(n)
