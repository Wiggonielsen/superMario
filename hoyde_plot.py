#plot
import matplotlib.pyplot as plt

pos = []
fart = []
tid = []

liste = []

with open('hoyde.csv','r') as f:
    for line in f:
        l = line.rstrip().split(';')#Splitter strengen ved ';' og fjerner linjeskift
        liste.append(l)


#22
for i in range(50,len(liste)-600):
    tid.append(float(liste[i][1]))
    pos.append(float(liste[i][2]))
    fart.append(float(liste[i][3]))

for i in range(650,len(liste)-2):
    tid.append(float(liste[i][1]))
    pos.append(float(liste[i][2]))
    fart.append(float(liste[i][3]))


plt.plot(tid,pos)
plt.title('Høyde over tid')
plt.ylabel('Meter')
plt.xlabel('Sekunder')


plt.savefig("hoyde.png") # Vi kan også lagre plot, gjør det før visning!
plt.show()  # Vis figur, og samtidig resett aktiv figur/axis@



