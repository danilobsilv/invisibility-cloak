import cv2
import numpy as np

global_frame = None
b, g, r = 0, 0, 0

def capture_background(cap, num_frames=60):
    # Captura o fundo para um número especificado de quadros
    for i in range(num_frames):
        ret, background = cap.read()
    return background

def mouseRGB(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN: #checks mouse left button down condition
        global b, g, r
        b = global_frame[y,x,0]
        g = global_frame[y,x,1]
        r = global_frame[y,x,2]


def main():
    cv2.namedWindow('cloack')
    cv2.setMouseCallback('cloack', mouseRGB)
    cap = cv2.VideoCapture(0)
    
    # Aguardando para capturar o fundo
    print("Posicione a câmera para capturar o fundo. Aguarde...")
    background = capture_background(cap)
    print("Fundo capturado.")

    global b, g, r

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Converte o frame de BGR para HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Define o intervalo da cor a ser escondida
        lower_bound = np.array([b - 60, g - 60, r - 60])
        upper_bound = np.array([b + 60, g + 60, r + 60])
        
        # Cria uma máscara para a cor especificada
        mask = cv2.inRange(frame, lower_bound, upper_bound)
        
        # Inverte a máscara
        mask_inv = cv2.bitwise_not(mask)
        
        # Extrai a parte do frame sem a cor a ser escondida
        frame_part = cv2.bitwise_and(frame, frame, mask=mask_inv)
        
        # Extrai a parte do fundo correspondente à cor a ser escondida
        background_part = cv2.bitwise_and(background, background, mask=mask)
        
        # Combina as duas partes
        result = cv2.addWeighted(frame_part, 1, background_part, 1, 0)
        
        global global_frame
        global_frame = result

        # Exibe o resultado
        cv2.imshow('cloack', result)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
