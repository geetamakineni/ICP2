
file= open("C:\\Users\\geeta\\PycharmProjects\\CLASS2\\Q3_txt.txt", "r")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word]=1
    else:
        wordcount[word] += 1

file=open("C:\\Users\\geeta\\PycharmProjects\\CLASS2\\output.txt","a")
file.write("\n")
file.write("Output:")
for i,j in wordcount.items():
    print (i,j)
    string=str(i)+" "+str(j)
    file.write("\n")
    file.write(string)
file.close();
