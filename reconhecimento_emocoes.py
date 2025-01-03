from deepface import DeepFace

class Emotions:
	def __init__(self, image_path, result_label):
		try:
			# análise de emoções
			result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)

			#Se for returnada uma lista guarda so a primeira cara
			if isinstance(result, list):
				result = result[0]

			# Extrair a informação e dar o resultado
			emotions_text = "Emotions and confidence scores:\n"
			for emotion, confidence in result['emotion'].items():
				emotions_text += f"{emotion.capitalize()}: {confidence:.2f}%\n"

			result_label.config(text=emotions_text)
		except Exception as e:
			print(f"Error analyzing the image: {e}")
