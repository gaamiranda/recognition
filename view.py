import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from reconhecimento_facial import Facial_recognition
from reconhecimento_emocoes import Emotions
import cv2
import numpy as np
import tempfile
import os

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
		tk.Button(frame, text="Pixelate", command=lambda: self.pixelize_image()).grid(row=0, column=3, padx=10)


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
	
	def pixelize_image(self, pixel_size=10, color_tint=(50, 50, 0)):
		if self.image_path:
			image = cv2.imread(self.image_path)

			# Pixalizar a imagem
			pixelized_image = cv2.resize(
				cv2.resize(image, (image.shape[1] // pixel_size, image.shape[0] // pixel_size)),
				(image.shape[1], image.shape[0]),
				interpolation=cv2.INTER_NEAREST
			)

			# Mudar a cor
			tinted_image = pixelized_image.astype(np.float32)
			tinted_image[:, :, 0] += color_tint[0]
			tinted_image[:, :, 1] += color_tint[1]
			tinted_image[:, :, 2] += color_tint[2]

			# Meter o valor dos pixeis entre 0 e 255
			tinted_image = np.clip(tinted_image, 0, 255).astype(np.uint8)

			resized_image = cv2.resize(tinted_image, (300, 300), interpolation=cv2.INTER_AREA)

			temp_dir = tempfile.gettempdir()
			temp_file_path = os.path.join(temp_dir, "pixelized_image.jpg")
			cv2.imwrite(temp_file_path, resized_image)

			# novo image path
			self.image_path = temp_file_path
			# Converter para o formato que o tkinter consegue ver
			tinted_image_pil = Image.fromarray(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
			img_tk = ImageTk.PhotoImage(tinted_image_pil)

			# update da label
			self.imagem_principal.config(image=img_tk)
			self.imagem_principal.image = img_tk
		else:
			tk.messagebox.showinfo(message="Imagem não selecionada")


#inicio
def main():
    root = tk.Tk()
    app = ImageApp(root)
    root.mainloop()
