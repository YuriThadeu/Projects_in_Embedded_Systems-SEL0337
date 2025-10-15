from gpiozero import LED, Button
from time import sleep
import os

# Chama a função para simular o Raspberry Pi
#from simulador_rpi import simular_raspberry_pi
#simular_raspberry_pi()


# Definir pinos
led = LED(27)  # pino GPIO 27 
button = Button(22,pull_up=True,bounce_time=0.05) # pino GPIO 10 com pull up ativado

# Definir função para ligar o LED quando o botão for pressionado
def button_pressed():
    led.on()
    os.system("clear")  # Tocar som em segundo plano
    print("Botão pressionado! LED aceso.")

# Definir função para desligar o LED quando o botão for solto
def button_released():
    led.off()
    os.system("clear")  # Tocar som em segundo plano
    print("Botão solto! LED apagado.")

# Vincular os eventos aos métodos
button.when_pressed = button_pressed
button.when_released = button_released

# Manter o programa rodando
while True:
    sleep(0.1)