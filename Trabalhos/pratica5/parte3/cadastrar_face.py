import cv2
import os

# Inicializa a câmera
cap = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

print("Posicione seu rosto na câmera.")
print("Pressione 's' para SALVAR a foto de referência e sair.")

while True:
    ret, frame = cap.read()
    if not ret: break

    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(grey, 1.1, 5)

    # Desenha o quadrado para você saber que está sendo detectado
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Verifica se apertou 's'
        if cv2.waitKey(1) & 0xFF == ord('s'):
            # Recorta apenas o rosto para salvar
            rosto_ref = frame[y:y+h, x:x+w]
            # Redimensiona para um tamanho padrão (ajuda na comparação)
            rosto_ref = cv2.resize(rosto_ref, (200, 200))
            # Salva o arquivo
            cv2.imwrite("usuario_mestre.jpg", rosto_ref)
            print(">> Rosto cadastrado com sucesso como 'usuario_mestre.jpg'!")
            cap.release()
            cv2.destroyAllWindows()
            exit()

    cv2.imshow("Cadastro de Usuario", frame)