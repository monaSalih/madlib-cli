import re

print ("Welcom to our madlib game i hope you enjoying, please answer the question right to built your story")
def read_template(filePath):
    openFile=open(filePath)
    # readFile=openFile.read
    return openFile.read()

def parse_template(upDateText):
    """
    in this function we split new sentene and add it to list fter that remove adjective from inter sentence 
    by using regeicx ,and after that commpined into new sentence 
    """
    parseEmp=''
    newTestList=[]
    addTextToList=upDateText.split(' ')
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

def output_file(result):
    with open("assets/game_output.txt", "w") as f:
        f.write(result)

     
def game_data():
    game_text = read_template("assets/make_me_a_video_game_template.txt")
    new_text, text_saved = parse_template(game_text)
    game_input = []
    for i in range(len(text_saved)):
        x = input('enter a {} > '.format(text_saved[i]))
        game_input.append(x)
    result = new_text.format(*game_input)
    print(result)
    output_file(result)

    

# get_data()