"""
Program: bandw.py
Author: Brian 

Computes the RGB value average of each pixel , if the average is closer to 0, the pixel will be black. If the average is closer to 255, the pixel will be whites.

"""
from images import Image

def blackAndWhite(image):
	"""Converts the argument image to pure black and white"""
	blackPixel = (0,0,0)
	whitePixel = (255, 255, 255)

	# Nested loop structure for traversing the image grid
	for y in range(image.getHeight()):
		for x in range (image.getWidth()):
			(r, g, b) = image.getPixel(x,y)
			average = (r + g + b) // 3
			if average < 128:
				image.setPixel(x, y, blackPixel)
			else:
				image.setPixel(x, y, whitePixel)

def main(filename = "smokey.gif"):
	image = Image(filename)
	print("Close the image window to continue.")
	image.draw()
	blackAndWhite(image)
	print("Close the image window to quit.")
	image.draw()

if __name__ == "__main__":
	main()