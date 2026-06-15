# st=input("Enter string")
# for c in st:
#     if st.count(c)==1:
#         print(f"{c} occurs only once")
#         break
# else:
#     print("All chars are repeating")

# st=input("Enter string")
# res=""
# for c in st:
#     if c not in res:
#         res+=c
# print(res)

# compress a string
#   aaaabcccddeee
#   a4b1c3d2e3
# st="aaaabcccddeee"
# res=""
# count=1
# for idx in range(0,len(st)-1):
#     if st[idx]==st[idx+1]:
#         count+=1
#     else:
#         res=res+st[idx]+str(count)
#         count=1
# print(res)

# st=input("Enter STring")
# res=""
# for idx in range(0,len(st),2):
#     res=res+st[idx]*int(st[idx+1])
# print(res)


# Container types in python

# 1.List:
# []
# hetrogenous type of datatype
# dynamic(grow and shrink in size)
# data can be changed
# indexed,sequence type
# 2.tuple
# ()
# hetrogenous type of datatype
# it is readonly
# indexed,sequence type
# 3.set
# {}
# duplicates are not allowed
# not a sequence type
# no indexes
# 4.dict
# {}
# key value pairs
# key cannot be duplicate
# value can be anything
# key ----->int,float,str,tuple
# dynamic

# lst=[12,45,"werwetrwert",67.34,12,0,"qwe",45]
# # print(lst[2:5])
# lst[2]="aadfh"
# print(lst)


# lst=list()
# for i in range(1,6):
#     num=int(input("Enter number"))
#     lst.append(num)
# print(lst)

# lst=[12,4,67,9]
# lst.insert(1,707)
# print(lst)

# lst=list(range(1,101))
# print(lst)

# lst=[1]*100
# print(lst)

# lst=[12,56,89,90,67,9]
# for idx,x in enumerate(lst):
#     print(idx,"              ",x)

# lst=["richa","raman","amit","ritu","raghav","334"]
# lst.sort(reverse=True)
# print(lst)
# print(max(lst))
# print(min(lst))
# mean=sum(lst)/len(lst)
# print(mean)


# 1.wap to print prefect squares from a list of numbers
# 2.wap to print total bill of customer
#     prices=[200,4000,350]
#     qty=[3,1,2]
# 3.lst=[rolno,name,89,67,89,56,84]
#   lst=[rolno,name,totmarks]
# 4.wap to remove all duplicates from list
# 5.wap to print largest word based on len from a string











