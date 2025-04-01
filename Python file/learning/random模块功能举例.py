import random
#设置随机数的种子
random.seed(10)#随机种相同所产生的随机数也相同
print(random.random())#0.0到1.0但是不包含1。[0, 1)
print(random.random())#按ctrl点击函数可以看到函数源码的解释

random.seed(10)
print(random.randint(1,100))#含1和100的数[a, b]

for i in range(10):
    print(random.randrange(1,10,3),end="\t")

print()
print(random.uniform(1,100))#[a, b]

lst=[i for i in range(1,11)]
print(random.choice(lst))

#随机的排序
print(lst)
random.shuffle(lst)
print(lst)
random.shuffle(lst)
print(lst)