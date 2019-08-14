import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import csv

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

#membaca data text dan diimport ke dalam kodingan untuk diproses
def importdata():
    with open('data_train_PNN.txt') as f:
        reader = csv.reader(f, delimiter="\t")
        d = list(reader)
    return d

#fungsi untuk melakukan visualisasi data train
def plots(data):
    x1, x2, x3 = [], [], []
    for i in range(len(data)):
        #melakukan pemisahan untuk warna pad setiap kelas
        if data[i][3] == '0':
            colors = 'b'
        elif data[i][3] == '1':
            colors = 'r'
        elif data[i][3] == '2':
            colors = 'g'
    
        x1.append(float(data[i][0]))
        x2.append(float(data[i][1]))
        x3.append(float(data[i][2]))

        ax1.scatter(x1[i],x2[i],x3[i],c = colors,marker='o')
    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')
    ax1.set_zlabel('z axis')

    plt.show()

plots(importdata())