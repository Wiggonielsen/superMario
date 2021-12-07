from sense_hat import SenseHat
import time

offsetLeft = 1
offsetTop = 2

tall =[1,1,1,1,0,1,1,0,1,1,0,1,1,1,1,  # 0
       0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,  # 1
       1,1,1,0,0,1,0,1,0,1,0,0,1,1,1,  # 2
       1,1,1,0,0,1,1,1,1,0,0,1,1,1,1,  # 3
       1,0,0,1,0,1,1,1,1,0,0,1,0,0,1,  # 4
       1,1,1,1,0,0,1,1,1,0,0,1,1,1,1,  # 5
       1,1,1,1,0,0,1,1,1,1,0,1,1,1,1,  # 6
       1,1,1,0,0,1,0,1,0,1,0,0,1,0,0,  # 7
       1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,  # 8
       1,1,1,1,0,1,1,1,1,0,0,1,0,0,1]  # 9
       
def siffer(siffer,x,y,r,g,b):
  offset = siffer * 15 # bestemmer hvor i listen den starter basert på gitt siffer(tall[] er 15*10 stor)
  for i in range(offset,offset+15): #+15 slik at den tar kun en linje i listen tall
    xt = i % 3
    yt = (i-offset) // 3
    sense.set_pixel(xt+x, yt+y, r*tall[i], g*tall[i], b*tall[i])

def fulltTall(verdi):
  #Det er ike plass til minustegn med to siffer, brker derfor farger
  if verdi <= 0:
    farge = (0,0,255)
  else:
    farge = (255,0,0)
  #Blå er minus, og Rød er pluss
  abs_ver = abs(verdi)
  tier = abs_ver // 10 #Finner antall tiere som skal printes, kun nødvendig hvis verdi > 9
  ener = abs_ver % 10 #finner alle enere som skal printes
  if (abs_ver > 9): #Kaller funksjonen siffer en ekstra gang, til venstre, dersom tallet > 9
    siffer(tier, offsetLeft, offsetTop, farge[0],farge[1],farge[2])
  siffer(ener, offsetLeft + 4, offsetTop, farge[0],farge[1],farge[2])
  

sense = SenseHat()
sense.set_rotation(270)

def main():
  sense.clear()
  temp = int(sense.get_temperature())
  fulltTall(temp)
  time.sleep(0.7)
  return str(temp)

if __name__ == '__main__':
  main()
