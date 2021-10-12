import re

print ("")
def read_template(filePath):
    openFile=open(filePath)
    # readFile=openFile.read
    return openFile.read()

def parse_template(upDateText):
    parseEmp=''
    newTestList=[]
    addTextToList=upDateText.split(' ')
    print(addTextToList)
    AdjectiveReg=r"^{\w+}|\.$"
    for i in addTextToList:
        if re.match(AdjectiveReg,i)==None :
            parseEmp+=f"{i} "
        else :
            if i==addTextToList[-1]:
                parseEmp+='{}.'
                newTestList+=[i[1:-2]]
            else:
                newTestList+=[i[1:-1]]
                parseEmp+='{} '
    newTestList=tuple(newTestList)
    return (parseEmp,newTestList)

