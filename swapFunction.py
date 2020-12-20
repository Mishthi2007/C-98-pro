def swapFileData() :
    file1=input('enter the file name')
    file2=input('enter the name of other file')
    with open (file1,'r') as A :
        dataA=A.read()
    with open (file2,'r') as B :
        dataB=B.read()
    with open (file1,'w') as A :
        A.write(dataB)
    with open (file2,'w') as B :
        B.write(dataA)
swapFileData()