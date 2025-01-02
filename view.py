import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def abrir_explorador():
    caminho_arquivo = filedialog.askopenfilename(
        title="Selecione uma imagem",
        filetypes=(("Imagens", ".png .jpg .jpeg"), ("Todos os arquivos", ".*"))
    )
    if caminho_arquivo:
        img = Image.open(caminho_arquivo)
        img = img.resize((300, 200))
        img_tk = ImageTk.PhotoImage(img)

        label_img.config(image=img_tk)
        label_img.image = img_tk 

janela = tk.Tk()
janela.title("Janela")
janela.geometry("500x300")

frame = tk.Frame(janela)
frame.pack(pady=20)

botao = tk.Button(frame, text="Browse", command=abrir_explorador)
botao.grid(row=0, column=0, padx=10)

botao2 = tk.Button(frame, text="Recognize")
botao2.grid(row=0, column=1, padx=10)

botao3 = tk.Button(frame, text="Pixelate")
botao3.grid(row=0, column=2, padx=10)

imagem_principal = tk.Label(janela)
imagem_principal.pack(pady=10)

janela.mainloop()
