from callFunctions import *
listy=[[2],[13,4,5],[[2]],2]
counter=Calls.setCounter(listy)
print("call:",Calls.call(listy,[0,0]),"\n\n")
while counter!=[]:
    result=Calls.movingCall(listy,counter)
    print("result:",result,"counter:",counter)
