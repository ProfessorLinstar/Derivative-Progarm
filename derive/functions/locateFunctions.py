class Locate:
    def locVar(inpStr,inpVar):
        varLocList = []
        for i in range(len(inpStr)):
            if inpVar==inpStr[i]:
                varLocList.append(i)
        return varLocList
