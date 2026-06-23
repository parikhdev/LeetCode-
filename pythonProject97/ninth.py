# import os
# with open("orig.txt","r") as fpsrc,open("chng.txt","w") as fpdst:
#     words=fpsrc.read().lower().split(" ")
#     for word in words:
#         if word in ["is","the","of"]:
#             fpdst.write("are ")
#         else:
#             fpdst.write(word+" ")
# os.remove("orig.txt")
# os.rename("chng.txt","orig.txt")


#
#
# list   []
# collection of hetrogenous type of data
# it can dynamically grow and shrink in size
# data is indexed
# it is ordered
# it is changable
#
# tuple  ()
# collection of hetrogenous type of data
# it is readonly,once created cannot be changed
# data is indexed
# it is ordered
#
# set   {}
# duplicates are not allowed
# collection of hetrogenous type of data
# it can dynamically grow and shrink in size
# data is not indexed
# it is not ordered
# it is changable but is diff
#
# dict   {101:"shalini",102:"raman"}
# it is a collection of key value pairs
# data is accessed using key
# dynamically grow and shrink
# changable
# key cannot be duplicate,value can be
# key can be int,float,str or a tuple

# lst=[23,56,89,"sfdsdgds",67.4,90,56,23,45,25]
# # lst.append(404)
# lst.insert(4,100)
# print(lst)

import random
lst=set()
while len(lst)!=10:
    r=random.randint(1,100)
    lst.add(r)
print(lst)

cnt=0
for x in lst:
    if x>20:
        cnt=cnt+1
print(f"Count of Nos greater than 20 is {cnt}")

























