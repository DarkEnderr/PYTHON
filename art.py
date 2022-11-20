import cv2
import time

image = cv2.imread(r"C:\Users\Win 8 64Bit VS7\Documents\Python\art.png", 0)

new_w = int(image.shape[1]/5)
new_h = int(image.shape[0]/5)

image = cv2.resize(image, (new_w, new_h))

charmap =" .,;:ox%#0"

with open("art.txt", 'x', encoding='utf-8') as f:
	for i, row in enumerate(image):
		for j, col in enumerate(row):
			c = int((255 - col)*10 / 256)
			f.write(charmap[c])
			print(charmap[c], end='')
		f.write('\n')
		print(charmap[c], end='')
		time.sleep(0.05)
	f.close()
			
