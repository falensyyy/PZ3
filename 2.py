import copy
num = [7,2,5]
num.append(4)
num.insert(1,10)
num.extend([1,1,1])
num.remove(7)
num.pop()
num.sort()
num.reverse()
num.count(2)
num.index(1)

num1 = num.copy()
num2 = copy.deepcopy(num)
num.clear()
print(num1,num2,num)
