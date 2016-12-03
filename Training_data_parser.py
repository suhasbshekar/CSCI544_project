import os
import json
import csv
jsonenc = json.JSONEncoder()
print("hi")
data=[]
with open("/Suhas/USC/NLP 544/Project/yelp_academic_dataset_review.json", "r", encoding="latin1") as file:
    # files = csv.reader(file)
    count=0
    for eachfile in file:
        if count==11000:
            break
        count = count + 1
        data.append(json.loads(eachfile))
    count=0
    psitive=0
    negative=0
    neutral=0
    for eachdata in data:
        if count==11000:
            break
        count = count + 1
        # print(eachdata)
        # try:
        #     os.remove('file'+str(count)+'.txt')
        # except OSError:
        #     pass
        # for each in eachfile:
        stars = eachdata['stars']
        if stars>3:
            psitive= psitive+1
            fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Train/positive/positive'+str(count)+'.txt', "w", encoding="latin1")
            fileWrite.write(str(eachdata['text']))
        elif stars<3:
            negative = negative + 1
            fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Train/negative/negative'+str(count)+'.txt', "w", encoding="latin1")
            fileWrite.write(str(eachdata['text']))
        elif stars==3:
            neutral = neutral + 1
            fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Train/neutral/neutral'+str(count)+'.txt', "w", encoding="latin1")
            fileWrite.write(str(eachdata['text']))
    print("positive ",psitive)
    print("negative ",negative)
    print("neutral ",neutral)
print("end")