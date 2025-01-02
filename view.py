import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from reconhecimento_facial import Facial_recognition

# Instantiate the recognition class
recognizer = Facial_recognition()

image_path = None

def abrir_explorador():
    global image_path
    image_path = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Imagens", ".png .jpg .jpeg"), ("Todos os arquivos", ".*"))
    )
    if image_path:
        img = Image.open(image_path)
        img = img.resize((300, 200))
        img_tk = ImageTk.PhotoImage(img)

        imagem_principal.config(image=img_tk)
        imagem_principal.image = img_tk  # Prevent garbage collection

def recognize_image():
    if image_path:
        recognizer.recognize_image(image_path)
    else:
        tk.messagebox.showinfo(message="Imagem não selecionada")

janela = tk.Tk()
janela.title("Janela")
janela.geometry("500x300")

frame = tk.Frame(janela)
frame.pack(pady=20)

botao_browse = tk.Button(frame, text="Browse", command=abrir_explorador)
botao_browse.grid(row=0, column=0, padx=10)

botao_recognize = tk.Button(frame, text="Recognize", command=recognize_image)
botao_recognize.grid(row=0, column=1, padx=10)

botao_pixelate = tk.Button(frame, text="Pixelate")
botao_pixelate.grid(row=0, column=2, padx=10)

imagem_principal = tk.Label(janela)
imagem_principal.pack(pady=10)

janela.mainloop()
