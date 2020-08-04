name = input("Enter file:")#taken file name as input
handle = open(name)#file opened
mail=dict()#creating an empty dictionary
for line in handle:#for every in in the text file
    if not line.startswith('From '):#if line doesn't starts with From
        continue# skip this iterartion and go to next
    else:#if it starts with From
         lst=line.split()#split the line into words and store it as lst
         mail[lst[1]]=mail.get(lst[1],0)+1#counting and inserting lst[1] into dictionary
bcount=None#bcount initialised to none
bword=None#bword initialised to None
for word,count in mail.items():
    if bcount is None or bcount<count:
        bcount=count#update bcount if the count is greater than ever since
        bword=word#update ther key correspndance to bcount
print(bword,bcount)#print the word and count of the word most repeated


#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
#The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
#The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear
# in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the
# most prolific committer.
