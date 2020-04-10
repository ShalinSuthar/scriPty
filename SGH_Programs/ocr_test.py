
from PIL import Image
import pytesseract
import argparse
import cv2
import os

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# construct the argument parse and parse the arguments

'''
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh",
	help="type of preprocessing to be done")
args = vars(ap.parse_args())
'''
def check(arg):
	args3=arg
	image=cv2.imread(args3)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

	cv2.imshow("Image", gray)


	'''
	if args["preprocess"] == "thresh":
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
	'''
	# make a check to see if median blurring should be done to remove
	# noise
	t=0
	b=1
	if t==1:
		gray = cv2.threshold(gray, 0, 255,
			cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

	elif b==1:
		gray = cv2.medianBlur(gray, 3)
	'''
	elif args["preprocess"] == "blur":
		gray = cv2.medianBlur(gray, 3)
	'''

	filename = "{}.png".format(os.getpid())
	cv2.imwrite(filename, gray)


	text = pytesseract.image_to_string(Image.open(filename))
	os.remove(filename)
	print(text)
	return text


cv2.waitKey(0)