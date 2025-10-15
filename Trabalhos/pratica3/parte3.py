import os
import time
import random
import signal
import RPi.GPIO as GPIO
from multiprocessing import Process, Event

# =========================
# CONFIGURAÇÕES
# =========================
# Numeração física (BOARD) para manter compatibilidade com o exemplo original.
# Se preferir BCM, troque para GPIO.setmode(GPIO.BCM) e ajuste o pino.
LED_BOARD_PIN = 7          # pino físico 7 (exemplo original)
BLINK_INTERVAL_S = 1.0     # período do pisca-pisca (s)
COUNT_INTERVAL_S = 2.0     # período da contagem aleatória (s)

# =========================
# FUNÇÕES DOS PROCESSOS
# =========================
def gpio_blink(stop_evt: Event, pin: int = LED_BOARD_PIN, interval: float = BLINK_INTERVAL_S):
    """Pisca um LED no pino indicado até o evento de parada ser acionado."""
    # Cada processo precisa configurar seu próprio contexto de GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)

    print(f"[Blink] PID={os.getpid()} | Iniciando pisca no pino BOARD {pin} (intervalo={interval:.1f}s)")

    try:
        state = False
        while not stop_evt.is_set():
            state = not state
            GPIO.output(pin, GPIO.HIGH if state else GPIO.LOW)
            print(f"[Blink] LED {'aceso' if state else 'apagado'}")
            time.sleep(interval)
    finally:
        # Limpeza apenas do pino usado por este processo
        try:
            GPIO.output(pin, GPIO.LOW)
        except Exception:
            pass
        GPIO.cleanup()
        print(f"[Blink] PID={os.getpid()} | Finalizado e GPIO liberado.")


def random_count(stop_evt: Event, interval: float = COUNT_INTERVAL_S):
    """Gera e exibe números aleatórios até o evento de parada ser acionado."""
    print(f"[Count] PID={os.getpid()} | Iniciando contagem aleatória (intervalo={interval:.1f}s)")
    try:
        while not stop_evt.is_set():
            count = random.randint(1, 100)
            print(f"[Count] valor: {count}")
            # Dorme em pequenos passos para responder rápido ao stop_evt
            t0 = time.time()
            while (time.time() - t0) < interval and not stop_evt.is_set():
                time.sleep(0.05)
    finally:
        print(f"[Count] PID={os.getpid()} | Finalizado.")


# =========================
# MAIN
# =========================
def main():
    stop_evt = Event()

    # Handler para Ctrl+C / SIGTERM
    def handle_signal(signum, frame):
        print(f"\n[Sinal] Recebido {signum}. Encerrando processos...")
        stop_evt.set()

    signal.signal(signal.SIGINT, handle_signal)   # Ctrl+C
    signal.signal(signal.SIGTERM, handle_signal)  # kill/stop

    p_blink = Process(target=gpio_blink, name="BlinkLED", args=(stop_evt,))
    p_count = Process(target=random_count, name="RandomCount", args=(stop_evt,))

    print("[Main] Iniciando processos...")
    p_blink.start()
    p_count.start()
    print(f"[Main] BlinkLED PID={p_blink.pid} | RandomCount PID={p_count.pid}")

    try:
        # Aguarda até que ambos encerrem (normalmente só após Ctrl+C)
        while p_blink.is_alive() or p_count.is_alive():
            time.sleep(0.2)
    finally:
        # Solicita parada
        stop_evt.set()

        # Tenta encerrar de forma graciosa
        for p in (p_blink, p_count):
            if p.is_alive():
                p.join(timeout=2.0)

        # Se ainda vivos, força término
        for p in (p_blink, p_count):
            if p.is_alive():
                print(f"[Main] Forçando término de PID {p.pid}...")
                p.terminate()
                p.join()

        print("[Main] Todos os processos finalizados.")

if __name__ == "__main__":
    main()
