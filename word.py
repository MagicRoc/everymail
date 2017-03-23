
def fetchword():
    theword = ""
    with open('value.txt',"r") as f1,open('recoad.txt',"r") as f2:
        flag = f2.read()
        count = 1
        for i in f1:
            count+=1
            if (count >= int(flag)):
                theword = theword + str(i) + "\n";
                if(count == int(flag)+10):
                    break
    with open("recoad.txt","w") as f:
        f.write(str(int(flag)+10))
    return theword

