import RPi.GPIO as GPIO
import time

# Configuração dos Pinos (Modo BCM)
LED_VERMELHO = 18
LED_VERDE = 17

# Desativa alertas de "canal em uso"
GPIO.setwarnings(False)
# Usa a numeração BCM (GPIO XX) e não o número físico do pino
GPIO.setmode(GPIO.BCM)

# Configura os pinos como SAÍDA
GPIO.setup(LED_VERMELHO, GPIO.OUT)
GPIO.setup(LED_VERDE, GPIO.OUT)

print("Iniciando Blink Alternado...")
print("Pressione Ctrl+C para parar.")

try:
    while True:
        # Estado 1: Vermelho LIGADO, Verde DESLIGADO
        GPIO.output(LED_VERMELHO, GPIO.HIGH)
        GPIO.output(LED_VERDE, GPIO.LOW)
        time.sleep(1) # Espera 1 segundo

        # Estado 2: Vermelho DESLIGADO, Verde LIGADO
        GPIO.output(LED_VERMELHO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.HIGH)
        time.sleep(1) # Espera 1 segundo

except KeyboardInterrupt:
    # Se você apertar Ctrl+C, o programa cai aqui
    print("\nParando...")

finally:
    # Limpa as configurações dos pinos ao sair (apaga tudo)
    GPIO.cleanup()
    print("Fim.")