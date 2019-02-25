from storeFunctions import *
inputList=[[["1",["2",[["2.5",["2.6","2.65"],"2.7",[["2.8"]],["2.9"]]]]],[["3"],["4","5"]],"6"],["7","8"],"9"]
output=Store.callStore(inputList,"-1",[0,1,1])


print("\n\ninputlist:",inputList,"\noutput:",output)

