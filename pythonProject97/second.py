# 1.wap to print prefect squares from a list of numbers
# 2.wap to print total bill of customer
#     prices=[200,4000,350]
#     qty=[3,1,2]
# 3.lst=[rolno,name,89,67,89,56,84]
#   lst=[rolno,name,totmarks]
# 4.wap to remove all duplicates from list
# 5.wap to print largest word based on len from a string

# from math import sqrt,isqrt
# lst=[23,45,68,49,12,16,98]
# for num in lst:
#     if sqrt(num)==isqrt(num):
#         print(num)

# prices=[230,3000,450,170]
# qty=[2,1,4,3]
# tot_amt=0
# print("Price\tQty\tAmt")
# for p,q in zip(prices,qty):
#     print(f"{p}\t{q}\t{p*q}")
#     tot_amt+=p*q
# print("Totabl Bill:" ,tot_amt)

# lst=[12,45,89,67,43,78,34,89]
# del(lst[2])
# if 70 in lst:
#     lst.remove(70)
# while True:
#     if 89 in lst:
#         lst.remove(89)
#     else:
#         break
# print(lst)

# lst=[101,"shalini",89,67,89,54,45]
# res=lst[2:]
# tot=sum(res)
# del(lst[2:])
# lst.append(tot)
# print(lst)

# lst=[1,2,4,5,7]
# lst1=list()
# lst1=lst1+lst
# lst[1]=9
# print(lst)
# print(lst1)

# lst=[1,2,3,4,2,5,6,3,7]
# # uniques=set(lst)
# # print(uniques)
# uniques=[]
# for num in lst:
#     if num not in uniques:
#         uniques.append(num)
# print(uniques)

# st=input("Enter string")
# lst=st.split(" ")
# for word in lst:
#     print(word,"      ",len(word))
# lst.sort(key=len)
# print(lst[-1])

# lst=[2,3,5,7,9,8,4]
# res=10
# ans=set()
# for num in lst:
#     cmp=res-num
#     if cmp in ans:
#         print((num,cmp))
#     ans.add(num)

# s=set()
# s.add(5)
# s.add(34)
# s.add(78)
# s.add(23)
# s.add(5)
# print(s[3])

# from random import randint
# s=set()
# while len(s)!=10:
#     r=randint(1,20)
#     s.add(r)
# print(s)

# questions=["2+2=","3-1="]
# qstppr=set()

# cstweb={1,3,4,7,9,11,15,17}
# cstoff={2,4,5,6,7,10,11,12,13}
# print("Customers shopping from botn web and offline")
# print(cstweb & cstoff)
# print("all customer")
# print(cstweb.union(cstoff))
# print("Only using web")
# print(cstweb-cstoff)

# t=(12,45,78,90,78,0)
# for idx,x in enumerate(t):
#     print(idx,"           ",x)

t=tuple("shalini")
print(t)















