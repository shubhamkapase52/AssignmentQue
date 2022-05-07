#find duplicate key
dict1={10:2,20:3,30:4,10:4,20:1}
dict2={}
for x in dict1:
    if x in dict2:
        dict2[x] += 1
    else:
        dict2[x] = 1
print(dict2)