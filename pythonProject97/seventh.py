# fp=open("myfile.txt","w")
# msg=input("Enter data")
# lines=msg.split(".")
# for line in lines:
#     fp.write(line+".\n")
# # fp.write(msg)
# fp.close()

# with open("myfile.txt","r") as fp:
#     for line in fp.readlines():
#         print(line)

    # data=fp.read(100)
    # # print(fp.tell())
    # fp.seek(0)
    # data1=fp.read()
    # print(data)
    # print(data1)

# netbal=0
# with open("transactions.txt","r") as fp:
#     for line in fp.readlines():
#         mode,amt=line.rstrip("\n").split(" ")
#         if mode=="D":
#             netbal+=(int)(amt)
#         elif mode=="W":
#             netbal-=(int)(amt)
# print(f"Net Balance is {netbal}")

with open("codefile.txt","r") as fp:
    for line in fp.readlines():
        if not line.strip(" ").startswith("//"):
            print(line.rstrip("\n"))























