from PIL import Image, ImageFilter

img = Image.open("./Pokedex/pikachu.jpg")


print(img)
#       <PIL.JpegImagePlugin.JpegImageFile image mode=RGB size=640x640 at 0x8A52C8>

print(img.format)
#       JPEG

print(img.size)
#       (640, 640)

print(img.mode)
# made is the coloring
#Red , Green , Blue
#       RGB

print(dir(img))
# look at to tarminal


filter_img_blur = img.filter(ImageFilter.BLUR)
# filter works only with png
# .seve("name.mode", "name of mode")
filter_img_blur.save("blur.png", "png")

# smooth
filter_img_smooth = img.filter(ImageFilter.SMOOTH)
filter_img_smooth.save("smooth.png", "png")

# sharpen
filter_img_sharpen = img.filter(ImageFilter.SHARPEN)
filter_img_sharpen.save("sharpen.png", "png")

# convert to other mode ,format
filter_img_bw = img.convert("L")
filter_img_bw.save("bw.png", "png")


# show img
# img to show.show()
#   filter_img_blur.show()
#   filter_img_bw.show()
#   filter_img_sharpen.show()
#   filter_img_smooth.show()

# rotate to rotate the img
# img.rotate(how many digrees)
filter_img_detail = img.filter(ImageFilter.DETAIL)
crooked_img = filter_img_detail.rotate(90)
crooked_img.save("detateed_and_rotated.png", "png")
# resize
resize_img = filter_img_detail.resize((200, 200))
resize_img.save("resize.png", "png")
print("this is the size of resize_img.png :", resize_img.size)

# crop to cut unneeded places
# crop needs a box so it can cut the img there
box = (200, 200, 400, 400)
croped_img = filter_img_detail.crop(box)
croped_img.save("crop.png", "png")


# make the img smaler
img2 = Image.open("./Pokedex/astro.jpg")
# you can do it with resize but it looks srinked ,because the rashou is defferent  12:2 and 1:1 or sme thig else
resize_img2 = img2.resize((400, 400))
resize_img2.save("resize_imag2.jpg",)
# so we use thumbnail workes like resize
# but thumbnail modifise the img
# so
img2.thumbnail((400, 400))
img2.save("thumbnail.jpg")
