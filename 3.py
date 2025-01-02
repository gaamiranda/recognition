import cv2
import numpy as np

# Certifique-se de instalar o pacote correto: opencv-contrib-python
# pip install opencv-contrib-python

# Inicializa o reconhecedor LBPH
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Exemplo de imagens de treino e seus rótulos
training_images = [
    cv2.imread("imgs/gm_feliz.jpg", cv2.IMREAD_GRAYSCALE),
    cv2.imread("imgs/gm_neutro.jpg", cv2.IMREAD_GRAYSCALE)
]

if not training_images:
	print("Error loading training_images")
	exit()

labels = [1, 2]  # Rótulos correspondentes às imagens de treinamento
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

# Carrega a imagem de teste e a prepara
test_image = cv2.imread("imgs/gm_neutro.jpg", cv2.IMREAD_GRAYSCALE)
test_image = cv2.resize(test_image, (100, 100))

# Prediz o rótulo e a confiança para a imagem de teste
label, confidence = recognizer.predict(test_image)
print(f"Rótulo previsto: {label}, Confiança: {confidence}")
