import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from reconhecimento_facial import Facial_recognition
from reconhecimento_emocoes import Emotions

class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Janela")
        self.root.geometry("800x600")

        # inicializar reconhecimento facial
        self.recognizer = Facial_recognition()

        # path da imagem principal
        self.image_path = None

        self.setup_ui()

    def setup_ui(self):
        # setup todo
        frame = tk.Frame(self.root)
        frame.pack(pady=20)

        # Butões
        tk.Button(frame, text="Browse", command=self.abrir_explorador).grid(row=0, column=0, padx=10)
        tk.Button(frame, text="Recognize", command=self.recognize_image).grid(row=0, column=1, padx=10)
        tk.Button(frame, text="Emotions", command=lambda: self.emotions_image()).grid(row=0, column=2, padx=10)
        tk.Button(frame, text="Pixelate").grid(row=0, column=3, padx=10)

        self.imagem_principal = tk.Label(self.root)
        self.imagem_principal.pack(pady=10)

        # label da imagem
        self.result_label = tk.Label(self.root, text="", font=("Helvetica", 16))
        self.result_label.pack(pady=10)

    def abrir_explorador(self):
        # sacar imagem e path
        self.image_path = filedialog.askopenfilename(
            title="Selecione uma imagem",
            filetypes=(("Imagens", ".png .jpg .jpeg"), ("Todos os arquivos", ".*"))
        )
        if self.image_path:
            img = Image.open(self.image_path)
            img = img.resize((300, 300))
            img_tk = ImageTk.PhotoImage(img)

            self.imagem_principal.config(image=img_tk)
            self.imagem_principal.image = img_tk
            self.result_label.config(text="")

    def recognize_image(self):
        if self.image_path:
            self.recognizer.recognize_image(self.image_path, self.result_label)
        else:
            self.result_label.config(text="Imagem não selecionada")

    def emotions_image(self):
        if self.image_path:
            Emotions(self.image_path, self.result_label)
        else:
            self.result_label.config(text="Imagem não selecionada")

#inicio
def main():
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
