import cv2
import numpy as np
import os

# Certifique-se de instalar o pacote correto: opencv-contrib-python
# pip install opencv-contrib-python

# Inicializa o reconhecedor LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()

# # Exemplo de imagens de treino e seus rótulos
# training_images = [
#     cv2.imread("imgs/gm_feliz.jpg", cv2.IMREAD_GRAYSCALE),
#     cv2.imread("imgs/gm_neutro.jpg", cv2.IMREAD_GRAYSCALE)
# ]

imgs_directory = "imgs/"
training_images = []
labels = []

for idx, filename in enumerate(os.listdir(imgs_directory)):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(imgs_directory, filename)
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        if image is not None:
            training_images.append(image)
            labels.append(idx)

if not training_images:
	print("Error loading training_images")
	exit()

if not labels or len(training_images) != len(labels):
    print("Error: Labels are missing or do not match the number of training images.")
    exit()

# Redimensiona todas as imagens para o mesmo tamanho
training_images = [cv2.resize(img, (100, 100)) for img in training_images]

# Converte as listas em arrays NumPy
training_images = np.array(training_images)
labels = np.array(labels)

# Treina o modelo
recognizer.train(training_images, labels)

# Carrega a imagem de teste
#Não esquecer que a imagem não pode estar na directoria imgs se quisermos um alto grau de confiança
test_image = cv2.imread("gui1.jpeg", cv2.IMREAD_GRAYSCALE)
test_image = cv2.resize(test_image, (100, 100))

# Prediz o rótulo e a confiança para a imagem de teste
label, confidence = recognizer.predict(test_image)
print(f"Rótulo previsto: {label}, Confiança: {confidence}")
