# Gera um PWM no GPIO18 para um LED, variando
# o duty cycle de 0% a 100% e depois a 0% 
# continuamente, o que faz o brilho subir e 
# descer suavemente.

import RPi.GPIO as GPIO
import time

PIN = 18          # pino GPIO 18
FREQ_HZ = 1000    # frequência do PWM

GPIO.setmode(GPIO.BCM) # usa a numeração BCM
GPIO.setup(PIN, GPIO.OUT) # configura o pino como saída

pwm = GPIO.PWM(PIN, FREQ_HZ) 
pwm.start(0)      # começa desligado (0%)

try:
    print("Iniciando varredura de brilho no LED...")
    while True:
        # sobe brilho 0 -> 100%a
        for dc in range(0, 101, 5): # de 0 a 100% em passos de 5%
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)
        # desce brilho 100 -> 0%
        for dc in range(100, -1, -5): # de 100 a 0% em passos de 5%
            pwm.ChangeDutyCycle(dc)
            time.sleep(0.01)

except KeyboardInterrupt:
    pass
finally:
    pwm.stop()
    GPIO.cleanup()
    print("PWM parado e GPIO liberado.")