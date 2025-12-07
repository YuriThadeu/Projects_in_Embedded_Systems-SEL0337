#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

# --- Configuração dos Pinos ---
LED_VERMELHO = 18
LED_VERDE = 17
PIN_BOTAO = 22  # Mesmo botão que você usou no reconhecimento

# --- Setup da Placa ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LEDs como Saída
GPIO.setup(LED_VERMELHO, GPIO.OUT)
GPIO.setup(LED_VERDE, GPIO.OUT)

# Botão como Entrada (Pull-Up: 1 solto, 0 apertado)
GPIO.setup(PIN_BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# --- Função Auxiliar ---
def esperar_com_verificacao(segundos):
    """
    Espera pelo tempo definido, mas verifica o botão a cada 0.1s.
    Retorna True se o botão for apertado, False se o tempo acabar.
    """
    passos = int(segundos / 0.1)
    for _ in range(passos):
        # Verifica se apertou (LOW porque é Pull-Up)
        if GPIO.input(PIN_BOTAO) == GPIO.LOW:
            return True 
        time.sleep(0.1)
    return False

print("--- MODO BLINK INICIADO ---")
print("Piscando LEDs alternados.")
print("Aperte o botão para encerrar tudo.")

try:
    while True:
        # --- ESTADO 1: Vermelho ON ---
        GPIO.output(LED_VERMELHO, GPIO.HIGH)
        GPIO.output(LED_VERDE, GPIO.LOW)
        
        # Espera 1 segundo, mas vigiando o botão
        if esperar_com_verificacao(1.0):
            print("\n>> Botão pressionado! Encerrando...")
            break # Sai do loop

        # --- ESTADO 2: Verde ON ---
        GPIO.output(LED_VERMELHO, GPIO.LOW)
        GPIO.output(LED_VERDE, GPIO.HIGH)

        # Espera 1 segundo, mas vigiando o botão
        if esperar_com_verificacao(1.0):
            print("\n>> Botão pressionado! Encerrando...")
            break # Sai do loop

except KeyboardInterrupt:
    print("\nInterrompido manualmente.")

finally:
    # Apaga tudo antes de sair
    GPIO.cleanup()
    print("Fim do programa.")