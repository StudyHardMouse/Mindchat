import time

a = 1

list1 = [1]
for i in range(29999999):
    a += 2
    c = -1/a
    a += 2
    d = 1/a
    list1.append(c)
    
    list1.append(d)
    
result = sum(list1) * 4
print('π最终结果：', result)
    