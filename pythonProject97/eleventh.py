# class Point:
#     def __init__(self,xx=0,yy=0):
#         self.x=xx
#         self.y=yy
#     def draw(self):
#         print(f"({self.x},{self.y})")
#         if self.x>=0 and self.y>=0:
#             print("First Quad")
#         elif self.x<0 and self.y>=0:
#             print("Second Quad")
#         elif self.x<0 and self.y<0:
#             print("Third Quad")
#         else:
#             print("Fourth Quad")
#
# p=Point(-3,7)
# p.draw()
#
#
# # p
# # 2344------------>x 0
# #                  y 0
#
#

# class Product:
#     def __init__(self,pid,pnam,pprc,pstk):
#         self.prdid=pid
#         self.prdnam=pnam
#         self.prdprc=pprc
#         self.prdstk=pstk
#     def showdet(self):
#         print(f"{self.prdnam} has price "
#               f"{self.prdprc} and stock {self.prdstk}")
#
# class Cart:
#     def __init__(self):
#         self.items=[]
#     def addproduct(self,prd):
#         self.items.append(prd)
#     def total(self):
#         return sum([prd.prdprc for prd in self.items])
#
# p=Product(101,"Ball Pen",25,10)
# p1=Product(102,"Notebook",120,20)
# p2=Product(103,"Marker",50,3)
# c=Cart()
# c.addproduct(p)
# c.addproduct(p2)
# print(f"Total Bill {c.total()}")

from mypack import account
a=account(101,"shalini",20000)
# print(a.__dict__)
a.deposit(5000)
a.displaybal()
a.withdraw(3000)
a.displaybal()














