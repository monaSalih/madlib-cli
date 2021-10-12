import re

print ("Welcom to our madlib game i hope you enjoying")
def read_template(filePath):
    openFile=open(filePath)
    # readFile=openFile.read
    return openFile.read()

def parse_template(upDateText):
    """
    in this function we split new sentene and add it to list after that remove adjective from inter sentence 
    by using regeicx ,and after that commpined into new sentence 
    """
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

   
def merge(upDateText,indexWord):
    """
    replace {} inside upDateText with index from indexWord by order 
    """
    return upDateText.format(*indexWord)
