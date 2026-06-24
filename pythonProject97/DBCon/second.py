# names=["shalini","shiven","raman","amit","atul","aneesh"]
# for name in names:
#     print(name.title())

# msg=input("ENter message")
# words=msg.split(" ")
# for word in words:
#     if len(word)>4:
#         print(word)


# lst=[12,45,78,90,67,0,7,91,34,23,34,4,6]
# for idx in range(0,len(lst)):
#     if idx==3 and idx==7:
#         lst[idx]=909
# print(lst)

# t=(12,45,67)
# print(t[0])
# prices=(30,23,45,678,90)
# qty=[2,0,0,1,3]
# totbil=0
# for p,q in zip(prices,qty):
#     totbil+=p*q
# print(f"Total Bill :{totbil}")

# s={12,45,67,89,34,78}
# s1={34,67,9,4,89,23,67,21}
# print(s-s1)

d={101:"shalini",102:"nidhi",103:"atul",104:"shiven"}
# d[105]="aaaaaaaaaaaaa"
# for k,v in d.items():
#     print(k,"             ",v)
# if 142 in d.keys():
#     print(d[142])
print(d.get(101,"no such key exists"))







