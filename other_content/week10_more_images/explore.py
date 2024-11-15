import cmpt120image as img_module
img_module.init()
img = img_module.get_image('./chatgpt_raccoon.jpg')
print(img[100][100])


# # beach_img = img_module.get_image('./Sunset_in_la_jolla.jpg')
# print(img[0])

# print(len(img))
# print(len(img[0]))

img_module.show_image(img, 'raccoon')

# # img_module.showImage(img[0:250], 'top half')

# # img_module.showImage(img[250:], 'bottom half')
input("Press enter to quit")