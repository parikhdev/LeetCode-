# def maxnum(num1,num2):
#     if num1>num2:
#         return num1
#     else:
#         return num2
#
# s=maxnum(45,23,67)
# print(s)

# def maxnum(*values):
#     maxi=0
#     for x in values:
#         if x>maxi:
#             maxi=x
#     return maxi
#
# t=maxnum(23,56,78)
# print("Maximum is ",t)

# def details(rolno,name,*marks):
#     print("Roll no :",rolno)
#     print("Name :",name)
#     print("Avg Score :",sum(marks)/len(marks))
#
# details(101,"shalini",8,56,89,78,56)

# def create_user(*args):
#     print("Creating user with details ",*args)
#
# def delete_user(*args):
#     print("Deleting user with details ",*args)
#
# def myfunc(func,*args):
#     func(*args)
#
# myfunc(create_user,"shalini","abc@gmail.com",True)
# myfunc(delete_user,"shalini")

# print("ewrwertert","sdgaertaer",sep="***",end="?")

# def createuser(**kwargs):
#     print(kwargs)
#
# createuser(id=101,name="shalini",age=47,is_active=False)

# def make_tag(tag,content,**attrs):
#     st=""
#     for key,value in attrs.items():
#         st=st+" "+key +"='"+value+"'"
#     return f"<{tag} {st}>{content}</{tag}"
#
# s=make_tag("a","Visit Google",href="https://google.com",target="_blank",size="12")
# print(s)

# def make_filters(**conditions):
#     query="Select * from tbproducts where "
#     cond=[]
#     for field,value in conditions.items():
#         cond.append(f"{field}='{value}'")
#     query=query+" and ".join(cond)
#     return query
#
# qry=make_filters(price=5000,size="L",brand="abc")
# print(qry)

# s=lambda x:x*2
# print(s(7))

# gt=lambda x,y:x if x>y else y
# print(gt(45,78))

# s=lambda :print("asfsad sdfg sdfg sdf g")
# s()

# lst=[[111,"shiven",32000],[102,"rahul",27000],[103,"amit",31000]]
# lst.sort(key=lambda x:x[2])
# print(lst)

# d=[{"empno":111,"name":"shiven","salary":34000},
# {"empno":101,"name":"raman","salary":41000},
# {"empno":121,"name":"aarav","salary":37000},
# {"empno":109,"name":"richa","salary":36000}
#    ]
# d.sort(key=lambda x:x["name"])
# print(d)

def pipeline(value,*funcs):
    for func in funcs:
        value=func(value)
    return value

s=pipeline(5,lambda x:x+3,lambda x:x*2,lambda x:x-1)
print(s)

# Comprehensions:
# map,filter,reduce










# <a href='https://google.com' target='_blank' >Visit Google</a>




