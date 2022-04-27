import math
import os
import matplotlib.pyplot as plt

# Config:
images_dir = 'img/photos'
result_grid_filename = './grid.jpg'
result_figsize_resolution = 40 # 1 = 100px
result_figsize_resolution2 = 40

images_list = os.listdir(images_dir)
images_count = len(images_list)
print('Images: ', images_list)
print('Images count: ', images_count)

# Calculate the grid size:
grid_size = math.ceil(math.sqrt(images_count))
plt.rcParams['axes.facecolor'] = 'black'

# Create plt plot:
fig, axes = plt.subplots(grid_size, grid_size, figsize=(result_figsize_resolution, result_figsize_resolution2))
#plt.axis('off')
#fig.get_yaxis().set_visible(False)
#plt.subplots_adjust(wspace=None, hspace=None)
current_file_number = 0
for image_filename in images_list:
	#plt.axis('off')
	x_position = current_file_number % grid_size
	y_position = current_file_number // grid_size
	plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace= 0, hspace= 0)
	plt_image = plt.imread(images_dir + '/' + images_list[current_file_number])
	axes[x_position, y_position].imshow(plt_image)
	axes[x_position, y_position].axis('off')
#	axes[x_position, y_position].set_facecolor('xkcd:salmon')

#	axes[x_position, y_position].set_visible(False)
	#plt.axis('off')
	#plt.subplots_adjust(wspace=5, hspace=5)
	print((current_file_number + 1), '/', images_count, ': ', image_filename)

	current_file_number += 1

plt.subplots_adjust(left=None, right=None, bottom=None, top=None, wspace=None, hspace=None)
plt.savefig(result_grid_filename, bbox_inches='tight', pad_inches = 0)

import sys
if sys.version_info[0] == 2:  # the tkinter library changed it's name from Python 2 to 3.
    import Tkinter
    tkinter = Tkinter #I decided to use a library reference to avoid potential naming conflicts with people's programs.
else:
    import tkinter
from PIL import Image, ImageTk

def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()    
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root,width=w,height=h)
    canvas.pack()
    canvas.configure(background='black')
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w/imgWidth, h/imgHeight)
        imgWidth = int(imgWidth*ratio)
        imgHeight = int(imgHeight*ratio)
        pilImage = pilImage.resize((imgWidth,imgHeight), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w/2,h/2,image=image)
    root.mainloop()

pilImage = Image.open("grid.jpg")
showPIL(pilImage)