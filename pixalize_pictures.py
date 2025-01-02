import cv2
import numpy as np

def pixelize_image(image, pixel_size=10, color_tint=(50, 50, 0)):
	# pixalizar a imagem
	pixelized_image = cv2.resize(
		cv2.resize(image, (image.shape[1] // pixel_size, image.shape[0] // pixel_size)),
		(image.shape[1], image.shape[0]),
		interpolation=cv2.INTER_NEAREST
	)

	# mudar a cor
	tinted_image = pixelized_image.astype(np.float32)
	tinted_image[:, :, 0] += color_tint[0]
	tinted_image[:, :, 1] += color_tint[1]
	tinted_image[:, :, 2] += color_tint[2]

	# pôr os pixeis num range entre 0 e 255
	tinted_image = np.clip(tinted_image, 0, 255).astype(np.uint8)

	return tinted_image
image = cv2.imread("gui1.jpeg")


pixelized_image = pixelize_image(image)

cv2.imshow("Pixelized Image", pixelized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
