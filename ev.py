def niharika(string):
    if len(string)%2==0:
        return "EVEN"
    else:
        return string[1]
names=["niha","anudeep"]
print(list(map(niharika,names)))