# import the Python Image processing Library
import PIL
from PIL import Image,ImageTk
import Tkinter as tk

# Code to add widgets will go here...


imageObject  = Image.open("./comp.jpg")
def image_crop(x1,y1,imageObject): 	
	cropped = imageObject.crop((x1,y1,x1+(imageObject.size[0]/10),y1+imageObject.size[1]/9))
	return cropped

def rgb_differnece(img1,img2):
	im = img1 # Can be many different formats.
	pix = im.load()
	print im.size  # Get the width and hight of the image for iterating over
	print pix[4,5][0]  # Get the RGBA Value of the a pixel of an image
	im2=img2
	pix2=im2.load()
	sum=0
	blue=0
	red=0
	green=0
	print type(pix2)
	raw1=[]
	

	for i in range(1,im.size[1]-1):
		try:
			red=(pix2[0,i-1][0]-pix[im.size[0]-1,i][0])
			blue =pix2[0,i][1]-pix[im.size[0]-1,i][1]
			green=pix2[0,i][2]-pix[im.size[0]-1,i][2]
			sum =sum+red+blue+green
		except:
			print(i,"not in picture")
	return sum

def crop_Array(imageObject):
	x1=0
	y1=0
	all_image=[[]]
	for i in range (9):
		for t in range (10):
			print("YOAV")
			all_image[i].append(image_crop(x1,y1,imageObject))
			y1=y1+(imageObject.size[1]/9)
		y1=0
		x1=x1+(imageObject.size[0]/10)
		all_image.append([])
	return all_image
def find_copule(img,img1):
	minNum=rgb_differnece(img1,img[0][0])
	nirImage=img[0][0]
	for i in range(len(img)-1):
		for t in range(len(img[0])-1):
			if rgb_differnece(img1,img[i][t])<minNum:
				minNum = rgb_differnece(img1,img[i][t])
				nirImage=img[i][t]
	return nirImage
img=[[]]
all_image=crop_Array(imageObject)

root = tk.Tk()
for i in range (9):
	for t in range (10):
		img[i].append(ImageTk.PhotoImage(crop_Array(imageObject)[i][t]))
	img.append([])
for g in range(9):
	for b in range (10):
			
			panel = tk.Label(root, image = img[g][b])
			panel.grid(row=b,column=g)


print("the sum is", rgb_differnece(all_image[0][0],all_image[0][1]))
print("the sum is",rgb_differnece(all_image[0][0],all_image[0][2]))
find_copule(all_image,all_image[4][5]).show()
all_image[4][5].show()
root.mainloop(  )