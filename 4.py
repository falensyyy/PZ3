values = [3,1,3,2,1,5,2]
uniq = set(values)
print(uniq)
print(len(uniq))
other = {2,4,5}
print(uniq & other)
print(uniq | other)
print(uniq - other)
print(other - uniq)
