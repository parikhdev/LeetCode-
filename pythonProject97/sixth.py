# customers=["abha","richa","nitin","naman","raman","amit","rohit"]
#
# def chkpallindrom(st):
#     if st==st[-1::-1]:
#         return True
#     else:
#         return False
#
# lst=(list)(filter(chkpallindrom,customers))
# print(lst)

# d={101:["shiven","sharma",25000,"SKL"],
#    102:["aarav","sharma",75000,"HSKL"],
#    103:["namit","sharma",31000,"SKL"]
#    }
# lst=(list)(filter(lambda x:True if d[x][3]=="SKL" else False,d))
# print(lst)
# namelst=(list)(map(lambda x:d[x][0]+" "+d[x][1],lst))
# print(namelst)

# orders=[[101,400,5],[102,3400,2],[103,2000,3]]
# lst=(list)(map(lambda x:[x[0],x[1]*x[2]] ,orders))
# print(lst)
# # res=[[101,2000],[102,6800],[103,6000]]
# dislst=(list)(map(lambda x:x if x[1]<5000 else [x[0],0.90*x[1]],lst))
# print(dislst)

# from functools import reduce
# words=["this","is","a","beautiful","day"]
# s=reduce(lambda x,y:x+len(y),words,0)
# print(s)
# marks=[67,89,45,89,34,78,37,58]
# s=reduce(lambda x,y:x if x>y else y,marks)
# print(s)
# x    y
# 0    67
# 67   89
# 89












