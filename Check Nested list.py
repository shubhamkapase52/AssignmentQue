#Check Weather List is Nested list or not if yes print "yes Nested List"else print "no"

list1=[1,2,3,4,[5,6,7,8]]

for x in list1:
    if type(x)==list:
        print(x)
        for a in x:
            print(a)
       
    
        

