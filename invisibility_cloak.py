import cv2
import numpy as np
import time


def invisibility_cloak(video_path):
    # Captura o vídeo
    capture_video = cv2.VideoCapture(video_path)

    # Aguarda a inicialização da câmera
    time.sleep(1)

    count = 0
    background = 0

    # Captura o fundo (primeiros 60 frames)
    for i in range(60):
        return_val, background = capture_video.read()
        if not return_val:
            continue

    background = np.flip(background, axis=1)

    # Processa o vídeo
    while capture_video.isOpened():
        return_val, img = capture_video.read()
        if not return_val:
            break
        count += 1
        img = np.flip(img, axis=1)

        # Converte a imagem de BGR para HSV
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Define a faixa de cor preta no espaço HSV
        lower_black = np.array([0, 0, 0])
        upper_black = np.array([180, 40, 40])

        # Gera uma máscara para detectar a cor preta
        mask = cv2.inRange(hsv, lower_black, upper_black)

        # Refina a máscara correspondente à cor preta detectada
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
        mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations=1)
        mask_inv = cv2.bitwise_not(mask)

        # Gera a saída final
        res1 = cv2.bitwise_and(background, background, mask=mask)
        res2 = cv2.bitwise_and(img, img, mask=mask_inv)
        final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

        cv2.imshow("INVISIBLE MAN", final_output)

        k = cv2.waitKey(10)
        if k == 27:
            break

    # Libera os recursos e fecha todas as janelas
    capture_video.release()
    cv2.destroyAllWindows()
