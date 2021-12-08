from sense_hat import SenseHat
from datetime import datetime
import time

a = 0.0065 #K/m
R = 287.06 #K/(Kg/K)
g0 = 9.81 #m/s**2
h1 = 0 #starthøyden kan fjernes, men gjør ingen skade, og gir muligheter som kan være praktiske
ant = 100 #antall målinger av trykket, dette gjøres for å filtrere bort feilmålinger
h_E = 3 #Høyde per etasje i meter

o = (0, 0, 0)
r = (100, 0, 0)
g = (0,100,0)

pause = [
    o,o,o,o,o,o,o,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,r,r,o,o,r,r,o,
    o,o,o,o,o,o,o,o
]

spill = [
    o,o,o,o,o,o,o,o,
    o,g,g,g,o,o,o,o,
    o,g,g,g,g,g,o,o,
    o,g,g,g,g,g,g,o,
    o,g,g,g,g,g,g,o,
    o,g,g,g,g,g,o,o,
    o,g,g,g,o,o,o,o,
    o,o,o,o,o,o,o,o
]

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

starttid = time.time()

sense = SenseHat()

def trykk():
    # ettersom trykket trengs i flere funksjoner valgte jeg å lage en egen funksjon for trykk som kan kalles
    sum = 0
    for i in range(ant): # kjører en forløkke som finner ett gjennomsnitt av ant antall målinger
        sum += float(sense.get_pressure())
        time.sleep(0.001)
    p0 = sum / ant #gjennomsnitt
    return p0

#setter ny referanse- trykk og temperatur
def kalibrer():
    p0 = trykk()
    #t0 = round(sense.get_temperature(),2) + 273.15
    t0 = 20.5 + 273.15 #rasberryen vil bli varmere ettersom den brukes. temperaturen inne vil likevell være stabil
    return p0,t0


def hoyde(p0,t0):
    p = trykk()
    h = (t0/a)*((p/p0)**(-a*R/g0)-1)+h1 #formelen for høyde basert på trykk
    return round(h,2) #runder til 2 decimaler, ettersom mm ikke er interessant for oppgaven og er utenfor sensorens feilmargin


def skrive(h):

    #teller antall ganger funksjonen er kjørt
    skrive.counter += 1
    
    #ved første måling vil det ikke være noen 'forrige linje' derfor settes start høyde og tid til 0
    if skrive.counter == 2:
        h1 = 0
        t1 = 0
    else:
        #henter ut de siste loggførte verdiene, dette brukes til å regne ut farten
        with open('hoyde.csv','r') as f:
            for line in f:
                pass
            siste = line.rstrip()
        liste = siste.split(';') # deler opp verdiene i csv filen errer ';'

        #verdiene i csv filen er formatert slik: målingnr;tid;høyde;fart
        # derfor er liste[1] forrige tidsmåling og liste[2] forrige høydemåling 
        t1 = float(liste[1])
        h1 = float(liste[2])


    with open('hoyde.csv','a') as f:

        #variabelen tid er anallet sekunder gått siden programmet begynnte
        tid = round(time.time() - starttid,1) #regner ut antall sekunder siden programmet startet å kjøre
        
        # skrive.counter brukes til å indeksere bakgrunnsmålingene, slik at dataen lettere kan hentes ut, 
        # og benyttes i senere tid
        f.write(str(skrive.counter))

        f.write(';' + str(tid) + ';')
        #dataen som lagres er høyden
        f.write(str(h))
        
        #Lagrer også hastigheten siste sekundet i m/s. Kan brukes til å kartlegge farten til heisen:)
        #ved å dele på tiden 
        f.write(';' + str(round((h - h1)/(tid - t1),2)) + '\n')


def maaling(h):
    maaling.counter += 1
    #henter klokkeslettet nå
    na = datetime.now()
    #formaterer det fint :)
    tidNa = na.strftime("%H:%M:%S")

    #benytter with open(...) as ... da denne lukker filen automatisk etter skriving
    #sørger dermed for færre programlinjer
    with open('målinger.csv','a') as f:
        f.write(str(maaling.counter) + ';' + str(tidNa) + ';' + str(h) + '\n')


def siffer(siffer,x,y,r,g,b):
  offset = siffer * 15 # bestemmer hvor i listen den starter basert på gitt siffer(tall[] er 15*10 stor)
  for i in range(offset,offset+15): #+15 slik at den tar kun en linje i listen tall
    xt = i % 3
    yt = (i-offset) // 3
    sense.set_pixel(xt+x, yt+y, r*tall[i], g*tall[i], b*tall[i])

def fulltTall(verdi):
  #Det er ike plass til minustegn med to siffer, brker derfor farger
  if verdi < 0:
    farge = (0,0,100)
  else:
    farge = (100,0,0)
  #Blå er minus, og Rød er pluss
  abs_ver = abs(verdi)
  tier = abs_ver // 10 #Finner antall tiere som skal printes, kun nødvendig hvis verdi > 9
  ener = abs_ver % 10 #finner alle enere som skal printes
  if (abs_ver > 9): #Kaller funksjonen siffer en ekstra gang, til venstre, dersom tallet > 9
    siffer(tier, offsetLeft, offsetTop, farge[0],farge[1],farge[2])
  siffer(ener, offsetLeft + 4, offsetTop, farge[0],farge[1],farge[2])


def etasje(h):
    # finner ved å heltallsdividere høyden over startposisjon på takhøyden i hver etasje
    e = int(h//h_E + 1)

    sense.clear()
    fulltTall(e)
    time.sleep(2)
    sense.clear()


def main():

    kjor = True

    #kalibrerer. Dette skjer kun en gang når programmet starter opp, slik at programmet har ett referansepunkt
    startverdier = kalibrer()
    p0 = startverdier[0]
    t0 = startverdier[1]

    #counter holder styr på hvor mange ganger de forskjellige funksjonene kjøres.
    #dette brukes til å indeksere målingene som gjøres
    skrive.counter = 1 
    maaling.counter = 0

    #viser et 'play' symbol for å illustrere at programmet har startet
    sense.set_pixels(spill)
    time.sleep(1)
    sense.clear()

    while kjor:
        h = hoyde(p0,t0)
        skrive(h) #sender den målte verdien for å skrives inn i csv fil

        #dokumenterer input fra bruker gjennom joysticken
        events = sense.stick.get_events()
        for event in events:
            if event.direction == 'left' and event.action == 'pressed':
                kalibrert = kalibrer()
                p0 = kalibrert[0]
                t0 = kalibrert[1]
                sense.show_message(str(round(p0,2)) + 'hPa')
                skrive.counter = 0

            elif event.direction == 'right' and event.action == 'pressed':
                maaling(h)
                sense.show_message(str(h) + 'm')
            
            elif event.direction == 'down' and event.action == 'pressed':
                sense.set_pixels(pause)
                e = sense.stick.wait_for_event()
                if e.direction == 'down':
                    kjor = False
                else:
                    sense.set_pixels(spill)
                    time.sleep(1)
                sense.clear()

            elif event.direction == 'up' and event.action == 'pressed':
                etasje(h)

        time.sleep(0.89)
            

main()