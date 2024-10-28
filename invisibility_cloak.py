import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk


def capture_background(cap, num_frames=60):
    # Captura o fundo para um número especificado de quadros
    background = None
    for _ in range(num_frames):
        ret, background = cap.read()
        if not ret:
            continue
    return np.flip(background, axis=1)


def get_color_range(color_name):
    # Definindo intervalos HSV para cores comuns, com ajustes aprimorados
    color_ranges = {
        'Vermelho': ([0, 120, 70], [10, 255, 255], [170, 120, 70], [180, 255, 255]),  # Adicionado segundo intervalo para vermelho
        'Verde': ([25, 40, 40], [85, 255, 255]),  # Ampliado intervalo de verde para captar tons mais claros e escuros
        'Azul': ([90, 40, 40], [130, 255, 255]),
        'Amarelo': ([20, 100, 100], [40, 255, 255]),  # Ajuste mais fino para melhorar a detecção do amarelo
        'Roxo': ([130, 50, 50], [170, 255, 255]),
    }
    return color_ranges.get(color_name, None)


def start_camera_with_color_selector():
    cap = cv2.VideoCapture(0)

    # Captura o fundo apenas uma vez
    print("Posicione a câmera para capturar o fundo. Aguarde...")
    background = capture_background(cap)
    print("Fundo capturado.")

    def update_invisibility_effect():
        selected_color = color_choice.get()
        color_range = get_color_range(selected_color) if selected_color else None

        ret, frame = cap.read()
        if not ret:
            return

        frame = np.flip(frame, axis=1)
        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        if color_range:
            # Extrai intervalo de cor selecionado
            if selected_color == 'Vermelho':
                lower_color1 = np.array(color_range[0])
                upper_color1 = np.array(color_range[1])
                lower_color2 = np.array(color_range[2])
                upper_color2 = np.array(color_range[3])

                # Cria duas máscaras para os diferentes tons de vermelho
                mask1 = cv2.inRange(hsv_frame, lower_color1, upper_color1)
                mask2 = cv2.inRange(hsv_frame, lower_color2, upper_color2)
                mask1 = cv2.bitwise_or(mask1, mask2)
            else:
                lower_color = np.array(color_range[0])
                upper_color = np.array(color_range[1])
                mask1 = cv2.inRange(hsv_frame, lower_color, upper_color)

            mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
            mask1 = cv2.dilate(mask1, np.ones((3, 3), np.uint8), iterations=1)
            mask2 = cv2.bitwise_not(mask1)

            # Combina o fundo e o quadro atual com a máscara
            res1 = cv2.bitwise_and(background, background, mask=mask1)
            res2 = cv2.bitwise_and(frame, frame, mask=mask2)
            result = cv2.addWeighted(res1, 1, res2, 1, 0)
        else:
            # Se nenhuma cor for selecionada, exibe apenas o frame atual
            result = frame

        # Mostra o resultado em tempo real
        cv2.imshow('Invisibility Cloak', result)

        # Verifica se o usuário apertou 'q' para sair
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            root.quit()  # Fecha a interface tkinter

        # Atualiza o loop da interface para processar o próximo frame
        root.after(10, update_invisibility_effect)

    # Configuração da janela tkinter para escolha de cor
    root = tk.Tk()
    root.title("Escolha a Cor da Capa de Invisibilidade")
    root.geometry("200x100")

    color_choice = tk.StringVar()
    color_choice.set("Selecione a cor")  # Texto inicial para o combobox

    label = ttk.Label(root, text="Selecione a cor:")
    label.pack(pady=5)

    # Dropdown para selecionar cor
    color_selector = ttk.Combobox(root, textvariable=color_choice)
    color_selector['values'] = ["Vermelho", "Verde", "Azul", "Amarelo", "Roxo"]
    color_selector.pack()

    # Inicia o efeito de invisibilidade em tempo real
    update_invisibility_effect()

    root.mainloop()
