def swapingFileData():
    file1=input("Give Original File: ")
    file2=input("Give the file to be swapped:")

    with open(file1, 'r') as a:
        data_a=a.read()
    with open(file2, 'r') as b:
        data_b=b.read()

    with open(file1, 'w+') as a:
        a.write(data_a)
    with open(file2, 'w+') as b:
        b.write(data_b)

swapingFileData()

 
