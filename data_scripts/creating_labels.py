import random
import os
import sys


data = open("./../data/wikisent2.txt","r")

l = data.readlines()

random.shuffle(l)

spec_char = ["%","*","{","}","[","]","#","<",">","`","~","|"]


dataset= l[:20000]


for s in spec_char:
    for item in dataset:
        if s in item:
            dataset.remove(item)
# max_len = 0
#
# for item in dataset:
#
#     if len(item)>max_len:
#         max_len = len(item)
#
# print(max_len)


for i,item in enumerate(dataset):

    dataset[i] = dataset[i][:50]


select_sent_train = dataset[:100]
select_sent_val = dataset[100:120]
select_sent_test = dataset[120:140]

with open('./../data/train.txt', 'w') as f:
    for item in select_sent_train:

        f.write("%s\n" % item)

with open('./../data/validation.txt', 'w') as f:
    for item in select_sent_val:

        f.write("%s\n" % item)

with open('./../data/test.txt', 'w') as f:
    for item in select_sent_test:

        f.write("%s\n" % item)