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
'''
count1 = 0
count0 = 0
with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt",'r',encoding='utf-8') as f:
    while(True):
        line = f.readline()
        if not line:
            break
            pass
        array = line.split("\t")
        #
        if len(array) == 4:
            count1 +=1

        else:
            count0 +=1
            print(array)
            print(len(array))
        # if count1 ==10000:
        #     break


print(count1)
print(count0)
'''
'''
data_test_list = []
with open(r"D:\\www\\data\\Weibo Data\\Weibo Data\\weibo_predict_data(new)\\weibo_predict_data.txt", 'r',
          encoding='utf-8') as f:
    while (True):
        line = f.readline()
        if not line:
            break
            pass
        array = line.split("\t")
        data_test_list.append([array[0], array[1]])


        print(data_test_list)

        break
        '''
dt = {}
dt["a"] =set()
dt["a"].add(1)
dt["a"].add(1)
print(dt)