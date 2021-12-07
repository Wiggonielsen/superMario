from sense_hat import SenseHat
import time

sense = SenseHat()

Y = (255, 255, 0)
B = (0, 0, 255)
R = (255, 0, 0)
W = (255,255,255)
flag_no = [
    R, R, W, B, B, W, R, R,
    R, R, W, B, B, W, R, R,
    W, W, W, B, B, W, W, W,
    B, B, B, B, B, B, B, B,
    B, B, B, B, B, B, B, B,
    W, W, W, B, B, W, W, W,
    R, R, W, B, B, W, R, R,
    R, R, W, B, B, W, R, R,
    ]
flag_se = [
    B, B, B, Y, Y, B, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, B, Y, Y, B, B, B,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    B, B, B, Y, Y, B, B, B,
    B, B, B, Y, Y, B, B, B,
    B, B, B, Y, Y, B, B, B,
    ]
flag_dk = [
    R, R, R, W, W, R, R, R,
    R, R, R, W, W, R, R, R,
    R, R, R, W, W, R, R, R,
    W, W, W, W, W, W, W, W,
    W, W, W, W, W, W, W, W,
    R, R, R, W, W, R, R, R,
    R, R, R, W, W, R, R, R,
    R, R, R, W, W, R, R, R,
    ]
flag_is = [
    B, B, W, R, R, W, B, B,
    B, B, W, R, R, W, B, B,
    W, W, W, R, R, W, W, W,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    W, W, W, R, R, W, W, W,
    B, B, W, R, R, W, B, B,
    B, B, W, R, R, W, B, B,
    ]

def main():
    heading = sense.get_compass()
    sense.clear()
    
    if heading < 45 or heading > 315:
      sense.set_pixels(flag_no)
    elif heading < 135:
      sense.set_pixels(flag_se)
    elif heading < 225:
      sense.set_pixels(flag_dk)
    else:
      sense.set_pixels(flag_is)
    
    
    return str(round(heading,2))


if __name__ == "__main__":
    while True:
        main()
        time.sleep(0.1)
