name = input("Enter file:")#input file name
handle = open(name)#open the file
data1=list()#creating an empty list
data2=dict()#creating an empty dictionary
for line in handle:#for every line in file
    if not line.startswith("From "):#if it doesn't startswith From
        continue
    else:
        line=line.split()#split the line if it starts with From
        data1.append(line[5])#append the hour into list
for time in data1:#creating dictionary of hour and count
    time=time.split(':')#splitting hour format
    data2[time[0]]=data2.get(time[0],0)+1#updating dictionary
for k,v in  sorted(data2.items()):#for sorted list of tuples printing its values and key i.e,hour and frequency
    print(k,v)
