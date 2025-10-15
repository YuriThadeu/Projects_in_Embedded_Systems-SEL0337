#!/usr/bin/env python3
# teste_hardware_interativo.py
# Menu interativo para testar LEDs, Servos (sweep continuo), Buzzer (PWM para piezo passivo)
# e DS18B20 no GPIO4 (padrao do Raspberry Pi). Cada teste roda ate CTRL+C; volta ao menu.
# Opcao 0 encerra com limpeza de GPIO.

import RPi.GPIO as GPIO
import time
import glob
import os
import sys
import subprocess

# =========================
# PINOS (BCM)
# =========================
GPIO_LED_VERDE   = 27
GPIO_LED_AMARELO = 22
GPIO_LED_VERM1   = 23
GPIO_LED_VERM2   = 24
GPIO_BUZZER      = 25
GPIO_SERVO1      = 18  # PWM0 (hardware)
GPIO_SERVO2      = 17  # PWM por software

# =========================
# SERVO / GERAIS
# =========================
SERVO_FREQ_HZ  = 50
SERVO_MIN_DUTY = 2.5   # ~1.0 ms
SERVO_MAX_DUTY = 12.5  # ~2.0 ms

# Sweep dos servos
SERVO_SWEEP_STEP_DEG = 2
SERVO_SWEEP_DT       = 0.02  # 50 Hz

# Buzzer passivo (piezo) - ajustes para maximo volume via GPIO (3.3V)
BUZZER_MAX_FREQ_HZ   = 3200   # frequencia tipica de pico (ajuste se quiser)
BUZZER_MAX_DUTY      = 50     # 50% costuma render maior SPL em piezo

# 1-Wire no GPIO4 (PADRAO)
# Com raspi-config (Interface Options -> 1-Wire -> Enable) o overlay vira:
# dtoverlay=w1-gpio  (sem gpiopin, o padrao e GPIO4)
W1_DEVICES_GLOB = "/sys/bus/w1/devices/28-*/w1_slave"
W1_BASE_DIR     = "/sys/bus/w1/devices"
CONFIG_TXT_PATH = "/boot/config.txt"

# =========================
# SUPORTE
# =========================
def angle_to_duty(angle):
    angle = max(0, min(180, angle))
    return SERVO_MIN_DUTY + (SERVO_MAX_DUTY - SERVO_MIN_DUTY) * (angle / 180.0)

def set_servo_angle(pwm, angle):
    pwm.ChangeDutyCycle(angle_to_duty(angle))

def setup_gpio():
    GPIO.setmode(GPIO.BCM)
    # Saidas simples
    for pin in (GPIO_LED_VERDE, GPIO_LED_AMARELO, GPIO_LED_VERM1, GPIO_LED_VERM2, GPIO_BUZZER):
        GPIO.setup(pin, GPIO.OUT, initial=GPIO.LOW)
    # Servos
    GPIO.setup(GPIO_SERVO1, GPIO.OUT)
    GPIO.setup(GPIO_SERVO2, GPIO.OUT)
    pwm1 = GPIO.PWM(GPIO_SERVO1, SERVO_FREQ_HZ)
    pwm2 = GPIO.PWM(GPIO_SERVO2, SERVO_FREQ_HZ)
    pwm1.start(0)  # duty 0 = sem pulso (descanso)
    pwm2.start(0)
    return pwm1, pwm2

def cleanup(pwm1=None, pwm2=None):
    try:
        if pwm1: pwm1.stop()
        if pwm2: pwm2.stop()
    except Exception:
        pass
    try:
        for pin in (GPIO_LED_VERDE, GPIO_LED_AMARELO, GPIO_LED_VERM1, GPIO_LED_VERM2, GPIO_BUZZER):
            GPIO.output(pin, GPIO.LOW)
    except Exception:
        pass
    try:
        GPIO.cleanup()
    except Exception:
        pass

def read_temp_raw_paths():
    """Retorna lista de caminhos w1_slave encontrados (ou vazia)."""
    return glob.glob(W1_DEVICES_GLOB)

def read_temp_c():
    """Le o primeiro DS18B20 encontrado. Retorna (temp_c, crc_ok, path) ou (None, False, path_ou_None)."""
    devs = read_temp_raw_paths()
    path = devs[0] if devs else None
    if not path:
        return None, False, None
    try:
        with open(path, "r") as f:
            lines = f.read().strip().splitlines()
        crc_ok = (len(lines) > 0 and lines[0].strip().endswith("YES"))
        temp_c = None
        if len(lines) > 1 and "t=" in lines[1]:
            parts = lines[1].split("t=")
            try:
                temp_c = int(parts[1]) / 1000.0
            except Exception:
                temp_c = None
        return temp_c, crc_ok, path
    except Exception:
        return None, False, path

def try_run(cmd):
    try:
        out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return 0, out.strip()
    except subprocess.CalledProcessError as e:
        return e.returncode, e.output.strip()
    except Exception as e:
        return -1, str(e)

def read_config_txt_lines():
    try:
        with open(CONFIG_TXT_PATH, "r") as f:
            return [ln.rstrip("\n") for ln in f.readlines()]
    except Exception:
        return []

# =========================
# TESTES
# =========================
def test_led(pin, nome):
    print(f"\n[LED {nome}] Piscando continuamente (0.5s ON / 0.5s OFF). CTRL+C para voltar ao menu.")
    try:
        while True:
            GPIO.output(pin, GPIO.HIGH); time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW);  time.sleep(0.5)
    except KeyboardInterrupt:
        GPIO.output(pin, GPIO.LOW)
        print("\nVoltando ao menu...")

def test_buzzer_max():
    """Buzzer passivo em 'maximo' via GPIO: PWM em 3.2 kHz, 50% duty, continuo."""
    print(f"\n[BUZZER (PASSIVO) - MODO MAXIMO GPIO] {BUZZER_MAX_FREQ_HZ/1000:.1f} kHz @ {BUZZER_MAX_DUTY}% duty.")
    print("CTRL+C para voltar ao menu.")
    pwm = None
    try:
        pwm = GPIO.PWM(GPIO_BUZZER, BUZZER_MAX_FREQ_HZ)
        pwm.start(BUZZER_MAX_DUTY)
        while True:
            time.sleep(1.0)
    except KeyboardInterrupt:
        pass
    finally:
        if pwm:
            pwm.stop()
        GPIO.output(GPIO_BUZZER, GPIO.LOW)
        print("\nVoltando ao menu...")

def test_buzzer_sweep():
    """Varre frequencias para achar a mais alta acusticamente no seu buzzer."""
    print("\n[BUZZER (PASSIVO) - VARREDURA DE FREQUENCIA] 1.5->4.5 kHz, 50% duty.")
    print("Ouça a variacao e identifique a faixa mais alta; depois use o modo MAXIMO.")
    print("CTRL+C para voltar ao menu.")
    pwm = None
    try:
        pwm = GPIO.PWM(GPIO_BUZZER, 1500)
        pwm.start(50)
        freqs = [1500, 1800, 2000, 2300, 2600, 3000, 3200, 3500, 3800, 4200, 4500]
        while True:
            for f in freqs:
                pwm.ChangeFrequency(f)
                print("  ->", f, "Hz")
                time.sleep(1.2)
    except KeyboardInterrupt:
        pass
    finally:
        if pwm:
            pwm.stop()
        GPIO.output(GPIO_BUZZER, GPIO.LOW)
        print("\nVoltando ao menu...")

def test_servo_sweep(pwm, nome):
    print(f"\n[{nome}] Sweep continuo 0°<->180° ate CTRL+C.")
    angle = 0
    direction = +1
    try:
        while True:
            set_servo_angle(pwm, angle)
            time.sleep(SERVO_SWEEP_DT)
            angle += direction * SERVO_SWEEP_STEP_DEG
            if angle >= 180:
                angle = 180; direction = -1
            elif angle <= 0:
                angle = 0;   direction = +1
    except KeyboardInterrupt:
        pwm.ChangeDutyCycle(0)  # descansar
        print("\nVoltando ao menu...")

def test_ds18b20_gpio4():
    """
    Diagnostico continuo do DS18B20 no GPIO4 (padrao):
      - checa se overlay padrao esta presente (dtoverlay=w1-gpio)
      - tenta carregar modulos (caso voce rode com sudo)
      - lista dispositivos 1-Wire e le temperatura/CRC
    """
    print("\n[DS18B20] Diagnostico continuo (GPIO4 - padrao). CTRL+C para voltar ao menu.")
    print("Fios: VDD=3.3V, GND=GND, DQ=GPIO4 (BCM, pino fisico 7), pull-up 4.7k para 3.3V.")
    print("Habilite 1-Wire pelo 'sudo raspi-config' (Interface Options -> 1-Wire -> Enable).")
    try:
        while True:
            # 1) Tentar carregar modulos (opcional; requer sudo)
            rc1, out1 = try_run(["sudo", "modprobe", "w1-gpio"])
            rc2, out2 = try_run(["sudo", "modprobe", "w1-therm"])
            print("\n-- modprobe -- w1-gpio:", "OK" if rc1 == 0 else "SKIP/FALHA",
                  "| w1-therm:", "OK" if rc2 == 0 else "SKIP/FALHA")

            # 2) Conferir diretorio do 1-Wire
            print("-- /sys/bus/w1/devices --")
            if not os.path.isdir(W1_BASE_DIR):
                print("X Diretorio nao existe:", W1_BASE_DIR)
                print("  -> Habilite 1-Wire e reinicie (raspi-config).")
                time.sleep(3.0)
                continue
            else:
                print("OK: Diretorio existe.")

            devs = read_temp_raw_paths()
            if devs:
                print("Dispositivos detectados:")
                for p in devs:
                    print("  -", p)
            else:
                print("ATENCAO: Nenhum dispositivo 28-xxxx detectado.")
                print("  Verifique fiacao, pull-up 4.7k e GPIO4.")

            # 3) Leitura
            temp, crc_ok, path = read_temp_c()
            if path:
                print("Arquivo de leitura:", path)
            if temp is None:
                print("Leitura: sem valor (CRC_OK =", crc_ok, ")")
            else:
                print("Temperatura:", f"{temp:.3f}", "C | CRC_OK:", crc_ok)

            print("-")
            time.sleep(2.0)
    except KeyboardInterrupt:
        print("\nVoltando ao menu...")

# =========================
# MENU
# =========================
def show_menu():
    print("\n========== TESTE DE HARDWARE ==========")
    print("1 - LED Verde")
    print("2 - LED Amarelo")
    print("3 - LED Vermelho1")
    print("4 - LED Vermelho2")
    print("5 - Servo 1 (GPIO18) - sweep continuo")
    print("6 - Servo 2 (GPIO17) - sweep continuo")
    print("7 - Buzzer (PASSIVO) - MAXIMO via GPIO (3.2 kHz / 50%)")
    print("8 - Buzzer (PASSIVO) - Varredura de frequencia (1.5->4.5 kHz)")
    print("9 - DS18B20 - Diagnostico (GPIO4 - padrao)")
    print("0 - Encerrar")
    print("=======================================")

def main():
    pwm1, pwm2 = setup_gpio()
    try:
        while True:
            show_menu()
            try:
                choice = input("Selecione o numero do teste: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nEncerrando...")
                break

            if choice == "1":
                test_led(GPIO_LED_VERDE, "Verde")
            elif choice == "2":
                test_led(GPIO_LED_AMARELO, "Amarelo")
            elif choice == "3":
                test_led(GPIO_LED_VERM1, "Vermelho1")
            elif choice == "4":
                test_led(GPIO_LED_VERM2, "Vermelho2")
            elif choice == "5":
                test_servo_sweep(pwm1, "Servo 1 (GPIO18)")
            elif choice == "6":
                test_servo_sweep(pwm2, "Servo 2 (GPIO17)")
            elif choice == "7":
                test_buzzer_max()
            elif choice == "8":
                test_buzzer_sweep()
            elif choice == "9":
                test_ds18b20_gpio4()
            elif choice == "0":
                print("Encerrando por solicitacao do usuario...")
                break
            else:
                print("Opcao invalida. Tente novamente.")
    finally:
        cleanup(pwm1, pwm2)
        print("GPIO liberado. Ate mais!")

if __name__ == "__main__":
    main()
