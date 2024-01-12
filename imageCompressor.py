from tkinter.filedialog import *

from PIL import Image

fl = askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality =10)