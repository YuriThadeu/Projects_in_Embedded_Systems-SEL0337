import cv2
import time
import RPi.GPIO as GPIO
import os

# --- Configurações de Hardware ---
PIN_LED_VERMELHO = 18
PIN_LED_VERDE = 17
PIN_BOTAO = 22  # Botão ligando ao GND
PIN_BUZZER = 27

# --- CONFIGURAÇÃO DO TEMPO (EM SEGUNDOS) ---
# Aqui é onde você modifica se quiser esperar mais ou menos tempo
TEMPO_LIMITE_DETECCAO = 3  

# --- Inicialização GPIO ---
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_LED_VERMELHO, GPIO.OUT)
GPIO.setup(PIN_LED_VERDE, GPIO.OUT)
GPIO.setup(PIN_BUZZER, GPIO.OUT)
GPIO.setup(PIN_BOTAO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

GPIO.output(PIN_LED_VERMELHO, GPIO.HIGH)
GPIO.output(PIN_LED_VERDE, GPIO.LOW)
GPIO.output(PIN_BUZZER, GPIO.LOW)

# --- Preparação da IA ---
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

if not os.path.exists("usuario_mestre.jpg"):
    print("ERRO: Foto 'usuario_mestre.jpg' não encontrada.")
    exit()

img_ref = cv2.imread("usuario_mestre.jpg")
hsv_ref = cv2.cvtColor(img_ref, cv2.COLOR_BGR2HSV)
hist_ref = cv2.calcHist([hsv_ref], [0, 1], None, [180, 256], [0, 180, 0, 256])
cv2.normalize(hist_ref, hist_ref, 0, 1, cv2.NORM_MINMAX)

cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

os.system('clear')
print("--- SISTEMA PRONTO ---")
print("Aperte o botão para solicitar acesso.")

try:
    while True:
        ret, frame = cap.read()
        if not ret: break

        # --- LÓGICA DO GATILHO ---
        if GPIO.input(PIN_BOTAO) == GPIO.LOW:
            
            os.system('clear')
            print(f">> Botão pressionado! Tentando detectar por {TEMPO_LIMITE_DETECCAO} segundos...")
            
            # Define o tempo limite (Agora + 3 segundos)
            fim_do_tempo = time.time() + TEMPO_LIMITE_DETECCAO
            usuario_identificado = False

            # --- LOOP DE TENTATIVA (Janela de Tempo) ---
            while time.time() < fim_do_tempo:
                # Lê um novo frame a cada tentativa para pegar movimento
                ret, frame = cap.read()
                if not ret: break

                grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_detector.detectMultiScale(grey, 1.1, 5)
                
                # Se achou rosto, verifica se é você
                if len(faces) > 0:
                    for (x, y, w, h) in faces:
                        rosto_live = frame[y:y+h, x:x+w]
                        try:
                            # Try/Except evita erro se o rosto for muito pequeno na borda
                            rosto_live = cv2.resize(rosto_live, (200, 200))
                            hsv_live = cv2.cvtColor(rosto_live, cv2.COLOR_BGR2HSV)
                            hist_live = cv2.calcHist([hsv_live], [0, 1], None, [180, 256], [0, 180, 0, 256])
                            cv2.normalize(hist_live, hist_live, 0, 1, cv2.NORM_MINMAX)

                            score = cv2.compareHist(hist_ref, hist_live, cv2.HISTCMP_CORREL)
                            
                            if score > 0.5:
                                usuario_identificado = True
                                # Salva as coordenadas para desenhar o quadrado final
                                rosto_coords = (x, y, w, h)
                                break 
                        except:
                            pass # Ignora erros de redimensionamento pontuais
                
                # Se já identificou, sai do loop de tempo imediatamente (não espera os 3s acabarem)
                if usuario_identificado:
                    break
            
            # --- RESULTADO FINAL APÓS O TEMPO ---
            if usuario_identificado:
                os.system('clear')
                print(">> ROSTO DETECTADO: Acesso Concedido.")
                print(">> Encerrando programa em 10 segundos...")
                
                # Desenha o quadrado na última imagem capturada
                (x, y, w, h) = rosto_coords
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, 'Yuri Thadeu', (x, y-10), font, 0.7, (0,255,0), 2)

                GPIO.output(PIN_LED_VERMELHO, GPIO.LOW)
                GPIO.output(PIN_LED_VERDE, GPIO.HIGH)
                
                cv2.imshow("Sistema", frame)
                cv2.waitKey(10000)
                break 
            
            else:
                os.system('clear')
                print(">> TEMPO ESGOTADO: Não detectado.")
                print(">> Tente novamente...")
                
                GPIO.output(PIN_LED_VERMELHO, GPIO.HIGH)
                
                for _ in range(3):
                    GPIO.output(PIN_BUZZER, GPIO.HIGH)
                    time.sleep(0.1)
                    GPIO.output(PIN_BUZZER, GPIO.LOW)
                    time.sleep(0.1)
                
                time.sleep(1.0) 

        else:
            # --- ESTADO INATIVO ---
            print("STATUS: Acesso Restrito - Aguardando botão...   ", end='\r')
            GPIO.output(PIN_LED_VERMELHO, GPIO.HIGH)
            GPIO.output(PIN_LED_VERDE, GPIO.LOW)

        cv2.imshow("Sistema", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nParando...")

finally:
    cap.release()
    cv2.destroyAllWindows()
    GPIO.cleanup()
    print("Programa Finalizado.")