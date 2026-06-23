from datetime import datetime as dt
hosts="C:\Windows\System32\drivers\etc\hosts"
print(dt.now())
dt1=dt(dt.now().year,dt.now().month,dt.now().day,9)
print(dt1)
dt2=dt(dt.now().year,dt.now().month,dt.now().day,12)
print(dt2)
block_sites=["www.instagram.com","instagram.com","www.msn.com","msn.com"]
redirect_to="127.0.0.1"
if dt1<=dt.now() and dt2>=dt.now():
    with open(hosts,"r+") as fp:
        content=fp.read()
        for site in block_sites:
            if site in content:
                pass
            else:
                fp.write(redirect_to+" "+site+"\n")
else:
    with open(hosts,"r+") as fp:
        lines=fp.readlines()
        fp.seek(0)
        for line in lines:
            if not any([site in line for site in block_sites]):
                fp.write(line)
        fp.truncate()
