from sys import argv
import os.path
import os
from PIL import Image
folder_name = argv[1]
new_folder_name = argv[2]
new_path = f"C:\\Users\\ShahZain\\Desktop\\python\\{folder_name}{new_folder_name}"
to_loop_path = f"C:\\Users\\ShahZain\\Desktop\\python\\{folder_name}"


def make_folder():
    try:
        os.mkdir(new_path)
        print("folder is created in :", new_path)
        for file_jpg in os.listdir(to_loop_path):
            if file_jpg.endswith(".jpg"):
                file_png = file_jpg.replace(".jpg", ".png")
                img = Image.open(f"{folder_name}{file_jpg}")
                img.save(f"{new_path}{file_png}", "png")
    except FileExistsError as err:
        print('FileExistsError : folder is allrady created')
        print("there is same folderin this path:", new_path)


make_folder()
