import os
import json
import csv
jsonenc = json.JSONEncoder()
print("hi")
data=[]
with open("/Suhas/USC/NLP 544/Project/yelp_academic_dataset_review.json", "r", encoding="latin1") as file:
    # files = csv.reader(file)
    count=0
    psitive = 0
    negative = 0
    neutral = 0
    for eachfile in file:
        if count==12000:
            break
        count = count + 1
        data.append(json.loads(eachfile))
    count=10001
    for eachdata in data:
        if count==12000:
            break
        if count > 10000:
            stars = eachdata['stars']
            if stars > 3:
                psitive = psitive + 1
                fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Dev/positive/positive' + str(count) + '.txt', "w",
                                 encoding="latin1")
                fileWrite.write(str(eachdata['text']))
            elif stars < 3:
                negative = negative + 1
                fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Dev/negative/negative' + str(count) + '.txt', "w",
                                 encoding="latin1")
                fileWrite.write(str(eachdata['text']))
            elif stars == 3:
                neutral = neutral + 1
                fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Dev/neutral/neutral' + str(count) + '.txt', "w",
                                 encoding="latin1")
                fileWrite.write(str(eachdata['text']))
            # fileWrite = open('/Suhas/USC/NLP 544/Project/Data/Dev/file' + str(count) + '.txt', "w",
            #                  encoding="latin1")
            # fileWrite.write(str(eachdata['text'].split()))
        count = count + 1
print("end")