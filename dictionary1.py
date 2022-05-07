# from Given list print 'harsha', print how many times letters are repeated and convert 'a' by any letters

list1 = [{'a':1, 'b':2, 'c':{1:2, 2:{'a':5, 'b':7, "c":'harsha'}}}]
print(list1[0]['c'][2]["c"])
x = list1[0]['c'][2]["c"]
print({i:x.count(i) for i in x})
k=x.replace("a","@")
print("modified harsha by:",k)



