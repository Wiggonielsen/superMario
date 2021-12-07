#trykk2

from sense_hat import SenseHat
import time

sense = SenseHat()
sense.set_rotation(270)

def main():
  press = sense.get_pressure()
  
  h = (255,255,255)
  b = (0,0,0)
  sense.show_message(str(round(press,2)), text_colour=h, back_colour=b, scroll_speed=0.1)

  return str(round(press,2))
  
if __name__ == '__main__':
  main()