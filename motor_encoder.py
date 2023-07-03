import RPi.GPIO as GPIO

usr_input = None
speed = 0

# 馬達接上A-、A+、B-、B+
# 另接12伏電壓供應
# 板子GND接RPI GND
# 連接PWM到腳位12
# 連接到任一腳位

GPIO.setmode(GPIO.BCM)

PWM_A = 12
PIN_A_PO = 5
PIN_A_NE = 6
encoder_pin_a = 17

PWM_B = 13
PIN_B_PO = 26
PIN_B_NE = 16
encoder_pin_b = 18

GPIO.setup(PWM_A, GPIO.OUT)
GPIO.setup(PWM_B, GPIO.OUT)

GPIO.setup(PIN_A_PO,GPIO.OUT)
GPIO.setup(PIN_A_NE,GPIO.OUT)
GPIO.setup(PIN_B_PO,GPIO.OUT)
GPIO.setup(PIN_B_NE,GPIO.OUT)

GPIO.setup(encoder_pin_a,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(encoder_pin_b,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)

pwm_a = GPIO.PWM(PWM_A, 1000)  # 设置PWM_A引脚为PWM输出模式，频率为100Hz
pwm_b = GPIO.PWM(PWM_B, 1000)  # 设置PWM_B引脚为PWM输出模式，频率为100Hz


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


def read_encoder():
  pass
  
try:
  while True:
    usr_input = input("command:")
    go_straight()
    go_back()
    stop()
    set_speed()


except KeyboardInterrupt:
  pass
