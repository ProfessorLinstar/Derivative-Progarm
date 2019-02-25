nestedList=[[[3],[2],[[4]],3],[[[[2,[3]],44],[3,4]],2]]
number=0
counter=[]
def nestedCall():#also adds moves counter to next one
    global counter
    global nestedList
    repeat=True
    while repeat:
        repeat=False
        i=nestedList
        number=0
        while type(i)==list:
            print("i",i,"number",number,"full counter:",counter)
            if len(counter)>number:
                if len(i)>counter[number]:
                    i=i[counter[number]]
                    number+=1
                else:
                    del counter[-1]
                    if len(counter)>0:
                        counter[-1]+=1
                    repeat=True
                    break
            elif len(counter)==0:
                return
            else:
                counter.append(0)
    if len(counter)>0:
        counter[-1]+=1
    number=0
    return i
#set first counter
i=nestedList
while type(i)==list:
    counter.append(0)
    i=i[0]
print(nestedList,"\n\n")

while len(counter)!=0:
    print("nestedcall:",nestedCall(),"counter:",counter,"\n\n")

