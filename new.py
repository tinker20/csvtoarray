with open ("new.txt", "r") as myfile:
    data=myfile.read().replace('\n', ',')
    print data
