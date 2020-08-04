name = input("Enter file:")
handle = open(name)
data1=list()
data2=dict()
data3=dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        line=line.split()
        data1.append(line[5])
for time in data1:
    time=time.split(':')
    data2[time[0]]=data2.get(time[0],0)+1
for k,v in  sorted(data2.items()):
    print(k,v)
