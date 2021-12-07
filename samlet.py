#samlet

import temp2
import trykk2
import hoyde2
import kompass3
from sense_hat import SenseHat
import time

sense = SenseHat()

ant_programmer = 4
cnt = 1

while True:
  for event in sense.stick.get_events():
    if event.direction == 'right' and event.action == 'pressed':
      cnt += 1
    elif event.direction == 'left' and event.action == 'pressed':
      cnt -= 1
    if cnt > ant_programmer:
      cnt = 1
    elif cnt < 1:
      cnt = ant_programmer

  time.sleep(0.1)

  f = open('verdier.csv','a')
  t = time.localtime()
  tid = time.strftime("%H:%M:%S", t)
  if cnt == 1:
    f.write('Temperatur klokken: ' + str(tid) + ' er: ' + temp2.main())
  elif cnt == 2:
    f.write('Trykk klokken: ' + str(tid) + ' er: ' + trykk2.main())
  elif cnt == 3:
    f.write('Høyde klokken: ' + str(tid) + ' er: ' + hoyde2.main())
  elif cnt == 4:
    f.write('Kompassretning klokken: ' + str(tid) + ' er: ' + kompass3.main())

  f.write('\n')
