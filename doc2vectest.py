from gensim.models.doc2vec import Doc2Vec
from nltk.tokenize import word_tokenize
model= Doc2Vec.load("d2v.model")
#to find the vector of a document which is not in training data
test_data = word_tokenize("Antibiotic use has been measured by checking the water near factory farms in China. Measurements have also been taken from animal dung.".lower())
v1 = model.infer_vector(test_data)
# print("V1_infer", v1)

# to find most similar doc using tags
similar_doc = model.docvecs.most_similar([v1])
# print(similar_doc)
data=[]
f=open("paragraphs.txt","r")
for x in f:
    data.append(x)
o=open("results.txt","w")
for i in range(0,10):
    o.write("RANK "+str(i+1)+'\n')
    print(similar_doc[i][0])
    o.write(data[int(similar_doc[i][0])])
    o.write("------------------------------------------------------\n")

# to find vector of doc in training data using tags or in other words, printing the vector of document at index 1 in training data
# print(model.docvecs['1'])