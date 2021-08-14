import csv
import re
import pandas as pd
import time
import os, psutil
list3=[[],[],[]]
process = psutil.Process(os.getpid()) 
memory = str(process.memory_info().rss)
#To write the performance into performance.txt file
def writePerfomance(start):
    p=open("Performance.txt","w")
    p.write("Time taken to process : " + str(time.time() - start) + " " + "seconds")
    p.write("\nMemory taken to process : " + memory + " bytes")
#The english words are replaced  french words
def change():
    reader = csv.reader(open('res/french_dictionary.csv', 'r'))
    d = {}
    for row in reader:
        i, j = row
        d[i] = j
    fin = open("t8.shakespeare.translated.txt", "wt")
    with open("res/t8.shakespeare.txt") as p:
        start_time = time.time()
        for line in p:
            list2=[]
            for words in line.split():
                if str("".join(re.findall("[a-zA-Z]+", words))) in d.keys():
                    list2.append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[0].append(str("".join(re.findall("[a-zA-Z]+", words))))
                    list3[1].append(d[str("".join(re.findall("[a-zA-Z]+", words)))])
                    list3[2].append(0)
                else:
                    list2.append(words)
            fin.write(" ".join(list2))
    print("Unique list of words that was replaced with French words from the dictionary\n\n")
    print(sorted(list(set(list3[0]))))
    print("\nTime to process:", time.time() - start_time, "seconds")
    print("\nMemory taken to process : " + memory + " bytes")
    print("\nTranslation done!")
    writePerfomance(start_time)
change()
df = pd.DataFrame({'English word': list3[0], 'French word': list3[1],'Frequency count':list3[2]})
df=(df.groupby(['English word','French word'])['Frequency count'].count())
df.to_csv('Frequency.csv') #Writing to Frequency.csv file
