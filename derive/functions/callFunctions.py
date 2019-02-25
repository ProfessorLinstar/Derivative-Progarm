class Calls:
    def setCounter(nestedList):
        counter=[]
        while type(nestedList)==list:
            counter.append(0)
            try:
                nestedList=nestedList[0]
            except IndexError:
                return []
        return counter
    def movingCall(nestedList,counter):
        repeat=True
        while repeat:
            repeat=False
            i=nestedList
            number=0
            while type(i)==list:
                #print("i",i,"number",number,"full counter:",counter)
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
        return i

    def moveCounter(nestedList,counter):
        #print("\nin move counter")
        repeat=True
        counter[-1]+=1
        while repeat:
            repeat=False
            i=nestedList
            number=0
            while type(i)==list:
                if len(counter)>number:
                    if len(i)>counter[number]:
                        i=i[counter[number]]
                        #print("next i:",i)
                        number+=1
                    else:
                        del counter[-1]
                        if len(counter)>0:
                            counter[-1]+=1
                        else:
                            return []
                        repeat=True
                        break
                else:
                    counter.append(0)
                    #print("i",i)
        #print("out of move counter\n\n")
        return counter


    def call(nestedList,counter):
        i=nestedList
        #print("\n\ncounter:",counter)
        for x in counter:
            i=i[x]
            #print("new i:",i)
        return i
