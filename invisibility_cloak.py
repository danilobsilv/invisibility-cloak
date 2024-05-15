import cv2
import numpy as np

def capture_background(cap, num_frames=60):
    # Captura o fundo para um número especificado de quadros
    background = None
    for _ in range(num_frames):
        ret, background = cap.read()
        if not ret:
            continue
    return np.flip(background, axis=1)


def invisibility_cloak():
    cv2.namedWindow('cloak')
    cap = cv2.VideoCapture(0)
    
    print("Posicione a câmera para capturar o fundo. Aguarde...")
    background = capture_background(cap)
    print("Fundo capturado.")

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = np.flip(frame, axis=1)

        # Converte o frame para o espaço de cores HSV
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Definir os intervalos de cor para detectar a cor da capa
        lower_blue = np.array([90, 40, 40])        
        upper_blue = np.array([130, 255, 255]) 
        mask1 = cv2.inRange(hsv_frame, lower_blue, upper_blue)
        
        # Refinar a máscara correspondente à cor detectada
        mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2) 
        mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1) 
        mask2 = cv2.bitwise_not(mask1)
    
        # Gerar a saída final 
        res1 = cv2.bitwise_and(background, background, mask=mask1) 
        res2 = cv2.bitwise_and(frame, frame, mask=mask2)
        result = cv2.addWeighted(res1, 1, res2, 1, 0)

        cv2.imshow('cloak', result)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    invisibility_cloak()
