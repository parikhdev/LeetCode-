# d={101:"shalini",102:"richa",104:"raman",105:"amit"}
# d[107]="shiven sharma"
# d[102]="Richa Sharma"
# d.pop(104)
# print(d)
# print(d.get(101,"No such key exists"))
# if 110 in d.keys():
#     print(d[110])
# for k,v in d.items():
#     print(k,"          ",v)

# for k in d:
#     print(k)
# print(d.keys())
# print(d.values())

# wap to count frequency of each char in a string
# this is india
#
# d={'t':1,'h':1,'i':2}
# st=input("Enter string")
# dic={}
# for c in st:
#     dic[c]=dic.get(c,0)+1
# print(dic)

# for c in st:
#     if c not in dic.keys():
#         dic[c]=1
#     else:
#         dic[c]=dic[c]+1
#     print(dic)
# print(dic)

# msg=input("Enter message").lower()
# words=msg.split(" ")
# freq={}
# for word in words:
#     freq[word]=freq.get(word,0)+1
# print(freq)

# names=["amit","raman","shiven","aarav","shalini","nidhi"]
# d={}
# for name in names:
#     c=name.lower()[0]
#     if c not in d.keys():
#         d[c]=[name]
#     else:
#         d[c]=d[c]+[name]
# print(d)

# print("\U0001F600")
# emotions={"happy":"\U0001F603","sad":"\U0001F62A",
#           "angry":"\U0001F621","laughing":"\U0001F596",
#           "sick":"\U0001F479"}
# msg=input("Enter your message")
# words=msg.split(" ")
# output=""
# for word in words:
#     if word in emotions.keys():
#         output=output+emotions[word]+" "
#     else:
#         output=output+word+" "
# print(output)

users={}
chc=""
while chc!="E":
    chc=input("Enter R to register,E to exit")
    if chc=="R":
        unam,upwd=input("Enter username,password").split(" ")
        if unam in users.keys():
            print("Username already exists.Try with other name")
        else:
            users[unam]=upwd
            print("Registration successful")
print(users)
