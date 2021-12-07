#hoyde

from sense_hat import SenseHat
import time

sense = SenseHat()
p0 = sense.get_pressure()
t0 = round(sense.get_temperature(),2) + 273.15
a = 0.0065 #K/m
R = 287.06 #K/(Kg/K)
g0 = 9.81 #m/s**2
h1 = 0

def hoyde(p):
  h = (t0/a)*((p/p0)**(-(a*R)/g0)-1)+h1
  print('h: ' + str(h))
  return h

def main():
  p = sense.get_pressure()
  h = round(hoyde(p),2)
  sense.show_message(str(round(hoyde(p),2)), text_colour=(100,100,100), back_colour=(0,0,0), scroll_speed=0.1)
  return str(round(hoyde(p),2))
if __name__ == '__main__':
    while True:
        main()
        time.sleep(0.1)
