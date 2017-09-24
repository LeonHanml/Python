# -*- coding: utf-8 -*-

'''
dict  = {}
dict[1] =[[1,2,3]]
dict[1].append([1,2,3])
print(dict)
# set(dict[1])
# for i in dict
print(dict)
'''
'''
list =[]
list.append("a")
array = [list]
array.append(list)
array.append([list,list])
a =set()
a.add("a")
a.add("a")
if "a" in a:
    print("true")

for i in a:
    print(i)
for i in array:
    print(i)
user_counts = map("a",[])
i=0
with open("") as f:
    # while  True:
    while i< 5:
        line_list = f.readline().split("\t")
        user_counts[line_list[0]] = line_list[3:5]
        i+=1
#     print( user_counts)
'''