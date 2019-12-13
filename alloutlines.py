from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
ps = PorterStemmer() 
f = open("outlines.txt", "r")
g = open("outlinecollection.txt", "w")
outlines={}
for x in f:
    if(x[0]=='=' and x[1]!='='):
        # words = word_tokenize(x[2:-2])
        # s=""
        # for w in words: 
        #     s=s+ps.stem(w)+" "
        if x[2:-2] in outlines:
            outlines[x[2:-2]]=outlines[x[2:-2]]+1
        else:
            outlines[x[2:-2]]=1

for x in outlines:
    if outlines[x]>=10:
        g.write(x+"\n")
    


   

