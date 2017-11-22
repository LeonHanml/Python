# def create_generator():
#     mylist = range(5)
#     print("---")
#     for i in mylist:
#         yield i*i
#
# mygenerator = create_generator()
# print(mygenerator)
#
# for i in mygenerator:
#     print(i)
#
#
# for i in mygenerator:
#     print(i)

#encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
        yield call(i)
        print("i2=",i)
        #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    print("call-",i)
    return i*2

#使用for循环
for i in yield_test(5):
    print(i,",")
