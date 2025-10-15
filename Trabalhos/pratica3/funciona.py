#!/usr/bin/env python3
# controle_temperatura_servos_leds_buzzer.py
# DS18B20 no GPIO4 (padrao), Servos (GPIO18 & GPIO17), LEDs e Buzzer
# Mostra painel em tempo real limpando a tela a cada leitura.

import glob, time, os, math, signal, sys
import RPi.GPIO as GPIO

# ===== 1-Wire no GPIO4 (habilite em: raspi-config -> Interface Options -> 1-Wire) =====
W1_DEVICES_GLOB = "/sys/bus/w1/devices/28-*"

# ===== GPIOs (BCM) =====
GPIO_LED_VERDE   = 27
GPIO_LED_AMARELO = 22
GPIO_LED_VERM1   = 23
GPIO_LED_VERM2   = 24
GPIO_BUZZER      = 25
GPIO_SERVO1      = 18
GPIO_SERVO2      = 17

# ===== Params =====
SERVO_FREQ_HZ   = 50
SERVO_MIN_DUTY  = 2.5
SERVO_MAX_DUTY  = 12.5

READ_TEMP_INTERVAL = 0.5
LOOP_DT            = 0.02
BUZZER_PERIOD      = 0.4

TH_A_MAX = 20.0
TH_B_MAX = 40.0
TH_C_MAX = 60.0
TH_D_MAX = 80.0
HYST     = 1.0

ENABLE_LOG_CSV = os.getenv("LOG_CSV", "0") == "1"
LOG_CSV_PATH   = os.getenv("LOG_PATH", "temperatura_log.csv")
ENABLE_SIM     = os.getenv("SIMULATE", "0") == "1"

# ===== Suporte =====
def angle_to_duty(angle):
    angle = max(0, min(180, angle))
    return SERVO_MIN_DUTY + (SERVO_MAX_DUTY - SERVO_MIN_DUTY) * (angle / 180.0)

def set_servo_angle(pwm, angle):
    pwm.ChangeDutyCycle(angle_to_duty(angle))

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    for pin in (GPIO_LED_VERDE, GPIO_LED_AMARELO, GPIO_LED_VERM1, GPIO_LED_VERM2, GPIO_BUZZER):
        GPIO.setup(pin, GPIO.OUT); GPIO.output(pin, GPIO.LOW)
    GPIO.setup(GPIO_SERVO1, GPIO.OUT)
    GPIO.setup(GPIO_SERVO2, GPIO.OUT)
    pwm1 = GPIO.PWM(GPIO_SERVO1, SERVO_FREQ_HZ)
    pwm2 = GPIO.PWM(GPIO_SERVO2, SERVO_FREQ_HZ)
    pwm1.start(0); pwm2.start(0)
    return pwm1, pwm2

def set_leds(verde=False, amarelo=False, verm1=False, verm2=False):
    GPIO.output(GPIO_LED_VERDE,   GPIO.HIGH if verde   else GPIO.LOW)
    GPIO.output(GPIO_LED_AMARELO, GPIO.HIGH if amarelo else GPIO.LOW)
    GPIO.output(GPIO_LED_VERM1,   GPIO.HIGH if verm1   else GPIO.LOW)
    GPIO.output(GPIO_LED_VERM2,   GPIO.HIGH if verm2   else GPIO.LOW)

def stop_servos(pwm1, pwm2):
    pwm1.ChangeDutyCycle(0); pwm2.ChangeDutyCycle(0)

def find_w1_device_path():
    devs = glob.glob(W1_DEVICES_GLOB)
    if not devs: return None
    return os.path.join(devs[0], "w1_slave")

def read_temp_c(path):
    try:
        with open(path, "r") as f:
            l1, l2 = f.read().strip().splitlines()
        if not l1.strip().endswith("YES"): return None
        parts = l2.split("t=")
        if len(parts) != 2: return None
        return int(parts[1]) / 1000.0
    except Exception:
        return None

def simulated_temp(t):
    return 52.5 + 42.5 * math.sin(t / 8.0)

class Sweep:
    def __init__(self, a_min=0, a_max=180, deg_per_sec=180, start=None, reverse=False):
        self.a_min, self.a_max = a_min, a_max
        self.pos   = a_min if start is None else max(a_min, min(a_max, start))
        self.dir   = -1 if reverse else +1
        self.speed = deg_per_sec
    def step(self, dt):
        self.pos += self.dir * self.speed * dt
        if self.pos >= self.a_max: self.pos = self.a_max; self.dir = -1
        elif self.pos <= self.a_min: self.pos = self.a_min; self.dir = +1
        return self.pos

class Saw:
    def __init__(self, a_min=0, a_max=180, deg_per_sec=180, start=None):
        self.a_min, self.a_max = a_min, a_max
        self.pos   = a_min if start is None else max(a_min, min(a_max, start))
        self.speed = deg_per_sec
    def step(self, dt):
        self.pos += self.speed * dt
        if self.pos >= self.a_max: self.pos = self.a_min
        return self.pos

def decide_faixa(temp_c, faixa_atual):
    if temp_c is None: return "DESCONHECIDA"
    if faixa_atual is None:
        if temp_c <= TH_A_MAX: return "A"
        if temp_c <= TH_B_MAX: return "B"
        if temp_c <= TH_C_MAX: return "C"
        if temp_c <= TH_D_MAX: return "D"
        return "E"
    if faixa_atual == "A":
        return "B" if temp_c > TH_A_MAX + HYST else "A"
    if faixa_atual == "B":
        if temp_c <= TH_A_MAX - HYST: return "A"
        if temp_c > TH_B_MAX + HYST:  return "C"
        return "B"
    if faixa_atual == "C":
        if temp_c <= TH_B_MAX - HYST: return "B"
        if temp_c > TH_C_MAX + HYST:  return "D"
        return "C"
    if faixa_atual == "D":
        if temp_c <= TH_C_MAX - HYST: return "C"
        if temp_c > TH_D_MAX + HYST:  return "E"
        return "D"
    if faixa_atual == "E":
        return "D" if temp_c <= TH_D_MAX - HYST else "E"
    return "DESCONHECIDA"

def cleanup(pwm1, pwm2):
    try: pwm1.stop(); pwm2.stop()
    except Exception: pass
    try:
        GPIO.output(GPIO_BUZZER, GPIO.LOW)
        set_leds(False, False, False, False)
        GPIO.cleanup()
    except Exception: pass
    print("Finalizado e GPIO liberado.")

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

# ===== Loop principal =====
def main():
    pwm1, pwm2 = setup_gpio()

    stop_flag = {"stop": False}
    def handle_sig(*_): stop_flag["stop"] = True
    for sig in (signal.SIGINT, signal.SIGTERM):
        signal.signal(sig, handle_sig)

    w1_path = None if ENABLE_SIM else find_w1_device_path()
    if not ENABLE_SIM and not w1_path:
        print("Aviso: DS18B20 nao encontrado em /sys/bus/w1/devices/.")
        print("Habilite 1-Wire (GPIO4) via raspi-config e verifique a fiacao/pull-up.")

    sweep_0_90   = Sweep(0,  90,  deg_per_sec=180)
    sweep1_180   = Sweep(0, 180, deg_per_sec=180, start=0,  reverse=False)
    sweep2_180   = Sweep(0, 180, deg_per_sec=180, start=90, reverse=True)
    saw_0_180    = Saw  (0, 180, deg_per_sec=180)

    last_temp_read = 0.0
    last_screen    = 0.0
    temp_c = None
    faixa  = None
    a1 = a2 = 0.0

    buzzer_on = False
    buzzer_t0 = time.time()

    if ENABLE_LOG_CSV and not os.path.exists(LOG_CSV_PATH):
        with open(LOG_CSV_PATH, "w") as f:
            f.write("timestamp,temp_c,faixa\n")

    print("Iniciando controle... Ctrl+C para sair.")
    try:
        while not stop_flag["stop"]:
            now = time.time()

            # Leitura de temperatura
            if (now - last_temp_read) >= READ_TEMP_INTERVAL or temp_c is None:
                if ENABLE_SIM or not w1_path:
                    temp_c = simulated_temp(now)
                else:
                    t = read_temp_c(w1_path)
                    if t is not None:
                        temp_c = t
                last_temp_read = now
                faixa = decide_faixa(temp_c, faixa)

                if ENABLE_LOG_CSV and temp_c is not None and faixa is not None:
                    try:
                        with open(LOG_CSV_PATH, "a") as f:
                            f.write(f"{int(now)},{temp_c:.3f},{faixa}\n")
                    except Exception:
                        pass

                # ---- Painel em tempo real (limpa tela) ----
                clear_screen()
                print("=== Controle Temperatura / Servos / LEDs / Buzzer ===")
                if w1_path:
                    print("Sensor:", w1_path)
                else:
                    print("Sensor: SIMULADO ou nao encontrado")
                print(f"Temperatura: {('---' if temp_c is None else f'{temp_c:.3f} °C')}")
                print(f"Faixa: {faixa}")
                print(f"Servos: a1={a1:.1f}°, a2={a2:.1f}°")
                print(f"Buzzer: {'ON' if buzzer_on else 'OFF'} (E somente)")
                print("Estados LEDs: ",
                      f"V={'1' if GPIO.input(GPIO_LED_VERDE) else '0'} ",
                      f"A={'1' if GPIO.input(GPIO_LED_AMARELO) else '0'} ",
                      f"R1={'1' if GPIO.input(GPIO_LED_VERM1) else '0'} ",
                      f"R2={'1' if GPIO.input(GPIO_LED_VERM2) else '0'} ", sep="")
                print("(Ctrl+C para encerrar)")

            # Ações por faixa
            if faixa == "A":
                set_leds(verde=True,  amarelo=False, verm1=False, verm2=False)
                stop_servos(pwm1, pwm2)
                GPIO.output(GPIO_BUZZER, GPIO.LOW)

            elif faixa == "B":
                set_leds(False, True,  False, False)
                a1 = sweep_0_90.step(LOOP_DT)
                set_servo_angle(pwm1, a1)
                pwm2.ChangeDutyCycle(0)
                GPIO.output(GPIO_BUZZER, GPIO.LOW)

            elif faixa == "C":
                set_leds(False, False, True,  False)
                a1 = sweep1_180.step(LOOP_DT)
                set_servo_angle(pwm1, a1)
                pwm2.ChangeDutyCycle(0)
                GPIO.output(GPIO_BUZZER, GPIO.LOW)

            elif faixa == "D":
                set_leds(False, False, True,  True)
                a1 = sweep1_180.step(LOOP_DT)
                set_servo_angle(pwm1, a1)
                a2 = saw_0_180.step(LOOP_DT)
                set_servo_angle(pwm2, a2)
                GPIO.output(GPIO_BUZZER, GPIO.LOW)

            elif faixa == "E":
                set_leds(False, False, True,  True)
                a1 = sweep1_180.step(LOOP_DT)
                a2 = sweep2_180.step(LOOP_DT)
                set_servo_angle(pwm1, a1)
                set_servo_angle(pwm2, a2)
                if (now - buzzer_t0) >= (BUZZER_PERIOD / 2.0):
                    buzzer_on = not buzzer_on
                    GPIO.output(GPIO_BUZZER, GPIO.HIGH if buzzer_on else GPIO.LOW)
                    buzzer_t0 = now
            else:
                set_leds(False, False, False, False)
                stop_servos(pwm1, pwm2)
                GPIO.output(GPIO_BUZZER, GPIO.LOW)

            time.sleep(LOOP_DT)

    except KeyboardInterrupt:
        pass
    finally:
        cleanup(pwm1, pwm2)

if __name__ == "__main__":
    main()
