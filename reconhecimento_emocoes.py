from deepface import DeepFace

# Path to the image
image_path = "imgs/gm_triste.jpg"

try:
	# análise de emoções
	result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

	#Se for returnada uma lista guarda so a primeira cara
	if isinstance(result, list):
		result = result[0]

	# Extrair a informação e dar o resultado
	print("Emotions and confidence scores:")
	for emotion, confidence in result['emotion'].items():
		print(f"{emotion.capitalize()}: {confidence:.2f}%")
except Exception as e:
	print(f"Error analyzing the image: {e}")
