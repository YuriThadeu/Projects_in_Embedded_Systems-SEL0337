from gpiozero import LED, Button
from time import sleep

# Definir pinos
led = LED(27)  # pino GPIO 27
button = Button(10)  # pino GPIO 10

# Definir função para ligar o LED quando o botão for pressionado
def button_pressed():
    led.on()

# Definir função para desligar o LED quando o botão for solto
def button_released():
    led.off()

# Vincular os eventos aos métodos
button.when_pressed = button_pressed
button.when_released = button_released

# Manter o programa rodando
while True:
    sleep(0.1)