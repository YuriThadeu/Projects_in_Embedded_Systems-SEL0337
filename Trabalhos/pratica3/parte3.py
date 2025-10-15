import time
import threading
import RPi.GPIO as GPIO

def led1_fade_worker(stop_event):
    """LED1 (GPIO27): fade 0→100→0 com frequência fixa e passo próprio."""
    LED1_PIN  = 27     # BCM
    FREQ_HZ   = 1200   # Hz (mais alta para diferenciar do LED2)
    STEP      = 4      # passo de duty (%)
    DT        = 0.008  # s entre passos

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED1_PIN, GPIO.OUT, initial=GPIO.LOW)

    pwm = GPIO.PWM(LED1_PIN, FREQ_HZ)
    pwm.start(0)
    print(f"[LED1] Iniciado: freq={FREQ_HZ} Hz, step={STEP}%, dt={DT}s")

    try:
        while not stop_event.is_set():
            # Sobe
            dc = 0
            while dc <= 100 and not stop_event.is_set():
                pwm.ChangeDutyCycle(dc)
                time.sleep(DT)
                dc += STEP
            # Desce
            dc = 100
            while dc >= 0 and not stop_event.is_set():
                pwm.ChangeDutyCycle(dc)
                time.sleep(DT)
                dc -= STEP
    finally:
        pwm.stop()
        GPIO.cleanup(LED1_PIN)
        print("[LED1] Finalizado e GPIO liberado.")

def led2_fade_button_worker(stop_event):
    """
    LED2 (GPIO22): fade 0→100→0.
    Enquanto o botão (GPIO2, PUD_UP) estiver PRESSIONADO:
      - frequência = FREQ_HIGH
      - passo do duty = STEP_FAST (>= 3x do inicial)
    Ao SOLTAR, reverte para frequência baixa e passo inicial.
    """
    LED2_PIN    = 22     # BCM
    BUTTON_PIN  = 2      # BCM
    FREQ_LOW    = 200    # Hz (inicial — bem menor que LED1)
    FREQ_HIGH   = 1500   # Hz (quando pressionado)
    STEP_INIT   = 5      # passo de duty (%) inicial
    STEP_FAST   = STEP_INIT * 3  # 3x maior
    DT          = 0.010  # s entre passos
    BOUNCE_MS   = 50     # debounce leve; vamos detectar transições por leitura

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED2_PIN,   GPIO.OUT, initial=GPIO.LOW)
    GPIO.setup(BUTTON_PIN, GPIO.IN,  pull_up_down=GPIO.PUD_UP)  # botão → GND

    pwm = GPIO.PWM(LED2_PIN, FREQ_LOW)
    pwm.start(0)

    # Estado do botão (pull-up): HIGH = solto, LOW = pressionado
    last_pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW
    print(f"[LED2] Iniciado: freq_inicial={FREQ_LOW} Hz, step_inicial={STEP_INIT}%, "
          f"freq_press={FREQ_HIGH} Hz, step_press={STEP_FAST}%")

    def read_pressed():
        # Leitura simples + pequena espera para amortecer bounces
        pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW
        time.sleep(BOUNCE_MS / 1000.0)
        return pressed

    try:
        while not stop_event.is_set():
            # Decide parâmetros conforme estado do botão
            pressed = GPIO.input(BUTTON_PIN) == GPIO.LOW
            if pressed != last_pressed:
                # Transição detectada → confirma com quick debounce
                pressed = read_pressed()
                if pressed != last_pressed:
                    last_pressed = pressed
                    if pressed:
                        print(f"[BOTÃO] Pressionado! LED2 → freq={FREQ_HIGH} Hz, step={STEP_FAST}%")
                    else:
                        print(f"[BOTÃO] Solto! LED2 → freq={FREQ_LOW} Hz, step={STEP_INIT}%")

            cur_freq = FREQ_HIGH if last_pressed else FREQ_LOW
            cur_step = STEP_FAST if last_pressed else STEP_INIT
            pwm.ChangeFrequency(cur_freq)

            # --- Fade UP (0→100) com passo dinâmico (reavalia a cada iteração) ---
            dc = 0
            while dc <= 100 and not stop_event.is_set():
                pwm.ChangeDutyCycle(dc)
                time.sleep(DT)

                # Atualiza estado (pode mudar no meio do fade)
                pressed_now = GPIO.input(BUTTON_PIN) == GPIO.LOW
                if pressed_now != last_pressed:
                    pressed_now = read_pressed()
                    if pressed_now != last_pressed:
                        last_pressed = pressed_now
                        if last_pressed:
                            print(f"[BOTÃO] Pressionado! LED2 → freq={FREQ_HIGH} Hz, step={STEP_FAST}%")
                        else:
                            print(f"[BOTÃO] Solto! LED2 → freq={FREQ_LOW} Hz, step={STEP_INIT}%")

                cur_freq = FREQ_HIGH if last_pressed else FREQ_LOW
                cur_step = STEP_FAST if last_pressed else STEP_INIT
                pwm.ChangeFrequency(cur_freq)
                dc += cur_step  # passo dinâmico

            # --- Fade DOWN (100→0) idem ---
            dc = 100
            while dc >= 0 and not stop_event.is_set():
                pwm.ChangeDutyCycle(dc)
                time.sleep(DT)

                pressed_now = GPIO.input(BUTTON_PIN) == GPIO.LOW
                if pressed_now != last_pressed:
                    pressed_now = read_pressed()
                    if pressed_now != last_pressed:
                        last_pressed = pressed_now
                        if last_pressed:
                            print(f"[BOTÃO] Pressionado! LED2 → freq={FREQ_HIGH} Hz, step={STEP_FAST}%")
                        else:
                            print(f"[BOTÃO] Solto! LED2 → freq={FREQ_LOW} Hz, step={STEP_INIT}%")

                cur_freq = FREQ_HIGH if last_pressed else FREQ_LOW
                cur_step = STEP_FAST if last_pressed else STEP_INIT
                pwm.ChangeFrequency(cur_freq)
                dc -= cur_step  # passo dinâmico

    finally:
        pwm.stop()
        GPIO.cleanup([LED2_PIN, BUTTON_PIN])
        print("[LED2] Finalizado e GPIO liberado.")

def main():
    stop_event = threading.Event()
    t1 = threading.Thread(target=led1_fade_worker,        args=(stop_event,), name="LED1",     daemon=True)
    # declara thread do LED1
    t2 = threading.Thread(target=led2_fade_button_worker, args=(stop_event,), name="LED2_BTN", daemon=True)
    # declara thread do LED2 + botão

    print("Iniciando threads (LED1 e LED2+Botão).")
    print("→ Sem botão: LED1 1200 Hz / step=4%; LED2 200 Hz / step=5% (diferença clara).")
    print("→ Botão pressionado (GPIO2): LED2 sobe p/ 1500 Hz e step=15% (>= 3x), soltou → volta ao normal.")

    t1.start(); t2.start() # inicia threads
    try:
        while t1.is_alive() and t2.is_alive():
            time.sleep(0.2)
    except KeyboardInterrupt: # verifica interrupção pelo usuário
        print("\n[Main] Encerrando (Ctrl+C).")
    finally:
        stop_event.set() # sinaliza threads para pararem
        t1.join(timeout=2.0) # aguarda threads encerrarem
        t2.join(timeout=2.0) # aguarda threads encerrarem
        try: GPIO.cleanup() # tenta liberar GPIOs (se não tiverem sido liberadas)
        except Exception: pass
        print("[Main] Fim.")

if __name__ == "__main__":
    main()
