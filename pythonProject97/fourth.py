# qstbnk={"2+2=":{"6":False,"4":True,"5":False,"None of above":False},
# "3-2=":{"1":True,"4":False,"5":False,"None of above":False},
# "12+2=":{"6":False,"14":True,"5":False,"None of above":False},
# "10-2=":{"6":False,"8":True,"5":False,"None of above":False},
# "24*2=":{"6":False,"4":False,"5":False,"48":True},
# "12-12=":{"6":False,"0":True,"5":False,"None of above":False},
# "15+2=":{"6":False,"4":False,"17":True,"None of above":False},
#         }
# import random
# paper=set()
# while len(paper)!=2:
#     lst=(list)(qstbnk.keys())
#     paper.add(random.choice(lst))
# score=0
# for qst in paper:
#     print("Qst :",qst)
#     print("Options:")
#     options=qstbnk.get(qst)
#     for k in options.keys():
#         print(k)
#     chc=input("Enter your answer")
#     if options.get(chc,False)==True:
#         score+=10
#     else:
#         score-=2.5
# print(score)
#
#

# def checkprime(num=2):
#     t=2
#     while t<num:
#         if num%t==0:
#             return False
#         t=t+1
#     return True
#
# if checkprime(27):
#     print("is prime")
# else:
#     print("is not prime")
# import time
# def time_ticker(nos=120):
#     while nos>0:
#         mins,secs=divmod(nos,60)
#         timer=f"{mins:02d}:{secs:02d}"
#         print("\r",timer,end="")
#         nos-=1
#         time.sleep(1)
#     print("\r","Time is up")
#
# time_ticker(20)
#
# def validate_email(emailid):
#     if "@" not in emailid:
#         return False
#     parts=emailid.split("@")
#     if len(parts)!=2:
#         return False
#     domain=parts[1]
#     if "." not in domain:
#         return False
#     return True
#
# print(validate_email("abc@gmailcom"))

# import re
# def validate_email(emailid):
#     pat=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
#     return re.match(pat,emailid) is not None
#
# eml=input("Enter your email")
# if validate_email(eml):
#     print("Email is valid")
# else:
#     print("invalid email")

# pwd length 6 to 12 chars
# should have an alphabet
# should have a digit
# should have a spl char
import string
def pwd_str(pwd):
    if len(pwd)<6 or len(pwd)>12:
        return False
    if not any([c.isalpha() for c in pwd]):
        return False
    if not any([c.isdigit() for c in pwd]):
        return False
    if not any([c in string.punctuation for c in pwd]):
        return False
    return True

print(pwd_str("1324s5#$"))
























