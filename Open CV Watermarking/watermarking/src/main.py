import cv2
import requests
import numpy as np
from PIL import Image
from io import BytesIO

def load_resize_image(url_image: str, resize: tuple = None):
	"""
	Loads an image from a given URL and optionally resizes it.

	Args:
	url_image (str): String containing the URL of the image.
	resize (tuple, optional): Tuple containing the new size of the image in the format (width, height). Defaults to None.

	Returns:
	Image (PNG/JPEG): The chosen image and logo.
	"""
	response = requests.get(url_image)
	image = Image.open(BytesIO(response.content))

	if resize:
		image = image.resize(resize)

	return image

# Extract height and width of the image
def extract_dimenstions(rgb_image, rgb_logo):
	height_image, width_image, _ = rgb_image.shape
	height_logo, width_logo, _ = rgb_logo.shape
	return height_image, width_image, height_logo, width_logo

# Return height and width values
def image_to_rgb(image, logo):
	rgb_image = np.array(image.convert("RGB"))
	rgb_logo = np.array(logo.convert("RGB"))
	height_image, width_image, height_logo, width_logo = extract_dimenstions(rgb_image, rgb_logo)
	return  rgb_image, rgb_logo, height_image, width_image, height_logo, width_logo

# Locate center of the image
def get_center_image(image, logo):
	rgb_image, rgb_logo, height_image, width_image, height_logo, width_logo = image_to_rgb(image=image, logo=logo)
	center_y = int(height_image/2)
	center_x = int(width_image/2)
	top_y = center_y - int(height_logo/2)
	left_x = center_x - int(width_logo/2)
	bottom_y = top_y + height_image
	right_x = left_x + width_logo

	return rgb_image, rgb_logo, center_y, center_x, top_y, left_x, bottom_y, right_x

# Select roi (Region Of Interest)
def region_of_interest(image, logo):
	rgb_image, rgb_logo, center_y, center_x, top_y, left_x, bottom_y, right_x = get_center_image(image, logo)
	roi = rgb_image[top_y: bottom_y, left_x: right_x]
	result = cv2.addWeighted(roi, 1, rgb_logo, 1, 0)
	return result