import sys
import os.path
import os
from PIL import Image
folder = sys.argv[1]
new_folder = sys.argv[2]
if not os.path.exists(new_folder):
    os.mkdir(new_folder)
    print("folder is created!")

for filename in os.listdir(folder):
    img = Image.open(f"{folder}{filename}")
    new_filename = (os.path.splitext(filename))[0]
    img.save(f"{new_folder}{new_filename}.png", "png")
print("files are saved as png!")
