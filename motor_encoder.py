import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

usr_input = None
speed = 0
encoder_count = 0
rotary_count = 0
PWM_A = 12
PIN_A_PO = 5
PIN_A_NE = 6
encoder_pin_a = 18

PWM_B = 13
PIN_B_PO = 26
PIN_B_NE = 16
encoder_pin_b = 17

GPIO.setup(PWM_A, GPIO.OUT)
GPIO.setup(PWM_B, GPIO.OUT)

GPIO.setup(PIN_A_PO,GPIO.OUT)
GPIO.setup(PIN_A_NE,GPIO.OUT)
GPIO.setup(PIN_B_PO,GPIO.OUT)
GPIO.setup(PIN_B_NE,GPIO.OUT)

GPIO.setup(encoder_pin_a,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(encoder_pin_b,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

pwm_a = GPIO.PWM(PWM_A, 2000)  
pwm_b = GPIO.PWM(PWM_B, 2000)  


pwm_a.start(0)
pwm_b.start(0)


def go_straight():
  if usr_input == "w":
    GPIO.output(PIN_A_PO,GPIO.HIGH)
    GPIO.output(PIN_A_NE,GPIO.LOW)
    GPIO.output(PIN_B_PO,GPIO.HIGH)
    GPIO.output(PIN_B_NE,GPIO.LOW)
  
def go_back():
  if usr_input =="s":
    GPIO.output(PIN_A_NE,GPIO.HIGH)
    GPIO.output(PIN_A_PO,GPIO.LOW)
    GPIO.output(PIN_B_NE,GPIO.HIGH)
    GPIO.output(PIN_B_PO,GPIO.LOW)

def turn_right():
  if usr_input == "d":
    GPIO.output(PIN_A_PO,GPIO.HIGH)
    GPIO.output(PIN_A_NE,GPIO.LOW)
    GPIO.output(PIN_B_NE,GPIO.HIGH)
    GPIO.output(PIN_B_PO,GPIO.LOW)
    
def turn_left():
  if usr_input == "a":
    GPIO.output(PIN_A_NE,GPIO.HIGH)
    GPIO.output(PIN_A_PO,GPIO.LOW)
    GPIO.output(PIN_B_PO,GPIO.HIGH)
    GPIO.output(PIN_B_NE,GPIO.LOW)

def stop():
  if usr_input == "k":
    GPIO.output(PIN_A_NE,GPIO.LOW)
    GPIO.output(PIN_A_PO,GPIO.LOW)
    GPIO.output(PIN_B_NE,GPIO.LOW)
    GPIO.output(PIN_B_PO,GPIO.LOW)

def set_speed():
  global speed
  if speed>=0 and speed<=100:
    if usr_input == "j":
      speed +=10
    elif usr_input == "l":
      speed -=10
  pwm_a.ChangeDutyCycle(speed)
  pwm_b.ChangeDutyCycle(speed)

def one_round():
  global encoder_count
  if usr_input == "n":
    count = 0
    while count <= 70:
      GPIO.output(PIN_A_NE,GPIO.LOW)
      GPIO.output(PIN_A_PO,GPIO.HIGH)
      GPIO.output(PIN_B_NE,GPIO.LOW)
      GPIO.output(PIN_B_PO,GPIO.HIGH)
      print(count)
    else:
      GPIO.output(PIN_A_NE,GPIO.LOW)
      GPIO.output(PIN_A_PO,GPIO.LOW)
      GPIO.output(PIN_B_NE,GPIO.LOW)
      GPIO.output(PIN_B_PO,GPIO.LOW)

      
def encoder_rotary(channel):
  global encoder_count,rotary_count
  encoder_count += 1
  if encoder_count >=68:
    rotary_count += 1 




GPIO.add_event_detect(encoder_pin_b, GPIO.BOTH, callback=encoder_rotary )

try:
  GPIO.output(PIN_A_NE,GPIO.LOW)
  GPIO.output(PIN_A_PO,GPIO.LOW)
  GPIO.output(PIN_B_NE,GPIO.LOW)
  GPIO.output(PIN_B_PO,GPIO.LOW)
  while True:
    usr_input = input("command:")
    one_round()
    go_straight()
    go_back()
    turn_left()
    turn_right()
    stop()
    set_speed()

except KeyboardInterrupt:
    GPIO.cleanup()
  
