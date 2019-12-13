import os
dir="/home/akshay/Sem1901/COL864/project/benchmarkY1-train.v2.0/benchmarkY1/benchmarkY1-train/"
# for files in os.listdir(dir):
#   flist=files.split('.')
# #   print(flist)
#   if (len(flist)>1 and flist[-2]=="cbor-paragraphs"):
#       print(files)
os.system("python3 /home/akshay/Sem1901/COL864/project/trec-car-tools/python3/test.py outlines "+dir+"train.pages.cbor-outlines.cbor >> outlines.txt")


