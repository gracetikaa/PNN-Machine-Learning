# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 12:59:55 2018

@author: gracetika
"""
import csv
import math
#membaca data text dan diimport ke dalam kodingan untuk diproses
def importdata(data):
    with open(data) as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
    return d
def eksportdata(text):
    with open('Hasil.txt', 'w') as text_file:
        writter = csv.writer(text_file,lineterminator = '\n')
        for line in text:
            writter.writerow([line])
            
#fungsi PNN dimana variable input adalah data train, att1 data tes, att2 data tes dan att3 data tes
def pnn(data,x,y,z):
#    s adalah variable smoothing
    s = 1
#    fxa,fxb,fxc adalah variable untuk melakukan sum pada setiap rumus 
    fxa,fxb,fxc = 0,0,0
    for i in range(len(data)):
        x1 = float(data[i][0])
        x2 = float(data[i][1])
        x3 = float(data[i][2])
        if data[i][3] == '0':
            fxa = fxa + math.exp(-1*((math.pow(x-x1,2)+math.pow(y-x2,2)+math.pow(z-x3,2))/(2*math.pow(s,2))))
        elif data[i][3] == '1':
            fxb = fxb + math.exp(-1*((math.pow(x-x1,2)+math.pow(y-x2,2)+math.pow(z-x3,2))/(2*math.pow(s,2))))
        elif data[i][3] == '2':
            fxc = fxc + math.exp(-1*((math.pow(x-x1,2)+math.pow(y-x2,2)+math.pow(z-x3,2))/(2*math.pow(s,2))))
            
    if fxa > fxb and fxa > fxc:
        return 0
    elif fxb > fxa and fxb > fxc:
        return 1
    elif fxc > fxa and fxc > fxb:
        return 2

train = importdata('data_train_PNN.txt')
tes = importdata('data_test_PNN.txt')
hasil = []
for i in range(len(tes)):
    Hpnn = pnn(train,float(tes[i][0]),float(tes[i][1]),float(tes[i][2]))
    hasil.append(Hpnn)
eksportdata(hasil)
