# Author :lixinhao
s = [1, 3, 5, 7, 0, -1, -9, -4, -5, 8]
m = [i for i in s if i > 0]
n = [i for i in s if i < 0]
print(len(m))
print(len(n))

ss = "axbyczdj"
print(ss[1:6:2])

qg = 'hello_world_yoyo'
print(qg.split('_'))

a = 1
print('%04d' %a)

aa = [1,3,5,7]
aa.insert(3,1)
print(aa[1:])

l1= []
for i in range(100,1000):
    sum = 0
    ss = list(str(i))
    for j in ss:
        sum += int(j)**3
        if sum == i:
            l1.append(i)
print(l1)

o = [1, 3, 10, 9, 21, 35, 4, 6]
yy = range(1,len(o))[::-1]
