from gpiozero import LED
from time import sleep
import os


# Chama a função para simular o Raspberry Pi
#from simulador_rpi import simular_raspberry_pi
#simular_raspberry_pi()

# Definir o pino do LED
led = LED(27)

# Função para contagem regressiva
def countdown_timer(total_seconds):
    seconds = int(total_seconds)  # Type casting para garantir formato inteiro
    while seconds > 0:
        led.off()  # Apaga o LED no início de cada ciclo
        minutos, segundos = divmod(seconds, 60)
        # Formatar MM:SS
        time_str = '{:02d}:{:02d}'.format(minutos, segundos)
        # Imprimir na mesma linha (sobrescreve a linha anterior)
        print(f"Tempo restante: {time_str}", end='\r', flush=True)

        sleep(1)

        seconds -= 1

    # Mostrar 00:00 antes de finalizar (garante que usuário veja o zero)
    minutos, segundos = divmod(0, 60)
    print(f"Tempo restante: {'{:02d}:{:02d}'.format(minutos, segundos)}", end='\n', flush=True)
    print("Contagem regressiva finalizada!")
    led.on()  # Acende o LED ao final


# Entrada de tempo e validação
while True:
    try:
        try:
            user_input = input("Digite o tempo para a contagem regressiva (em segundos): ")
            # Tentar converter para inteiro (type casting). Isso lança ValueError se inválido.
            time_input = int(user_input)
            os.system('clear')  # limpa tela uma vez antes da contagem
            if time_input <= 0:
                print("Por favor, insira um número de segundos positivo.")
            else:
                countdown_timer(time_input)
                #break  # se eu deixar esse, ele sai do loop após execução, mas vou manter o loop
                # para permitir múltiplas contagens sem reiniciar o programa
        except ValueError:
            os.system('clear')
            print("Valor inválido! Por favor, insira um número inteiro.")
    except KeyboardInterrupt:
        print("\nPrograma encerrado pelo usuário.")
        led.off()  # Apaga o LED ao sair
        break