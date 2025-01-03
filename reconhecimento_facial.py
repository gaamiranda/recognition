import cv2
import numpy as np
import os
import tkinter as tk

class Facial_recognition:
    def __init__(self):
        self.recognizer = cv2.face.LBPHFaceRecognizer_create()

        imgs_directory = "imgs/"
        training_images = []
        labels = []

        # preencher training images e label
        for idx, filename in enumerate(os.listdir(imgs_directory)):
            if filename.endswith(('.jpg', '.jpeg', '.png')):
                img_path = os.path.join(imgs_directory, filename)
                image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
                if image is not None:
                    training_images.append(image)
                    labels.append(idx)

        if not training_images:
            raise ValueError("Error loading training images")

        if not labels or len(training_images) != len(labels):
            raise ValueError("Labels are missing or do not match the number of training images")

        # Resize e preparar os dados
        training_images = [cv2.resize(img, (100, 100)) for img in training_images]
        training_images = np.array(training_images)
        labels = np.array(labels)

        # Treinar
        self.recognizer.train(training_images, labels)

    def recognize_image(self, path_to_img, result_label):
        if not path_to_img:
            raise ValueError("No path to image provided")

        test_image = cv2.imread(path_to_img, cv2.IMREAD_GRAYSCALE)
        test_image = cv2.resize(test_image, (100, 100))

        label, confidence = self.recognizer.predict(test_image)
        result_label.config(text=f"Parecença: {confidence:.2f}")
